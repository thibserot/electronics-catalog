import asyncio, json, re, sys
from pathlib import Path
from markdownify import markdownify as md
from playwright.async_api import async_playwright

DESKTOP_SELECTORS = [
    "#product-description", ".product-description", "#module_product_description",
    "#j-product-description", ".product-detail", "#product-detail"
]
MOBILE_SELECTORS = [
    "#product-detail", ".product-detail", "#product-description", ".product-description"
]
DESC_TAB_SELECTORS = [
    "text=Description", "#product-tabs a[href*='description']",
    "[role=tab]:has-text('Description')", "a#nav-description",
]

DIVIDER_MD = "\n\n---\n\n"

def normalize_and_extract_id(u: str) -> tuple[str, str | None]:
    """
    Returns (normalized_url, product_id or None).
    Normalizes accidental typos in /item/<id> and forces .html.
    """
    m = re.search(r"/item/([^/.]+)", u)
    pid = None
    if m:
        raw = m.group(1)
        pid = "".join(ch for ch in raw if ch.isdigit()) or None
        if pid:
            u = f"https://www.aliexpress.com/item/{pid}.html"
    return u, pid

async def click_description_tab(page):
    for sel in DESC_TAB_SELECTORS:
        try:
            loc = page.locator(sel)
            if await loc.count():
                await loc.first.click(timeout=2000)
                await page.wait_for_timeout(600)
                return True
        except:
            pass
    return False

async def pull_runparams(page):
    for expr in ("window.runParams", "window.run_params", "window.__AEP_PROPS__", "window.__AEP_DATA__"):
        try:
            rp = await page.evaluate(f"typeof {expr}==='object' ? {expr} : null")
            if isinstance(rp, dict):
                return rp
        except:
            pass
    return None

def deep_get(d, *path):
    cur = d
    for k in path:
        if isinstance(cur, dict) and k in cur:
            cur = cur[k]
        else:
            return None
    return cur

def norm_html(h: str) -> str:
    if not h: return ""
    h = re.sub(r"<script[\s\S]*?</script>", "", h, flags=re.I)
    h = re.sub(r"<style[\s\S]*?</style>", "", h, flags=re.I)
    h = re.sub(r"(?i)(<br\s*/?>\s*){3,}", "<br><br>", h)
    return h.strip()

async def extract_descriptions_from_selectors(page, selectors):
    out = []
    for sel in selectors:
        try:
            loc = page.locator(sel).first
            if await loc.count():
                html = await loc.inner_html()
                if html and len(html.strip()) > 30:
                    out.append(norm_html(html))
        except:
            pass
    return out

async def fetch_iframe_desc(ctx, page):
    results = []
    try:
        ifr = page.locator("iframe")
        n = await ifr.count()
        candidates = []
        for i in range(n):
            src = await ifr.nth(i).get_attribute("src")
            if not src: continue
            if any(h in src for h in ("desc.alicdn.com", "aeproducts.", "ae01.alicdn.com")):
                candidates.append(src)
        for src in candidates:
            try:
                resp = await ctx.request.get(src, timeout=60_000)
                if resp.ok:
                    html = await resp.text()
                    if html and len(html.strip()) > 30:
                        results.append(norm_html(html))
            except:
                continue
    except:
        pass
    return results

async def extract_all_descriptions(ctx, page, mobile=False):
    results = []
    # let dynamic bits settle
    for _ in range(3):
        try:
            await page.wait_for_load_state("networkidle", timeout=3000)
            break
        except:
            pass

    selectors = MOBILE_SELECTORS if mobile else DESKTOP_SELECTORS
    results += await extract_descriptions_from_selectors(page, selectors)

    await click_description_tab(page)
    results += await extract_descriptions_from_selectors(page, selectors)

    rp = await pull_runparams(page)
    if rp:
        # raw html
        for kp in [
            ("description",), ("data","description"), ("pageModule","description"),
            ("data","desc"), ("pageModule","desc"),
        ]:
            val = deep_get(rp, *kp)
            if isinstance(val, str) and len(val) > 30:
                results.append(norm_html(val))
        # descUrl
        for kp in [
            ("descUrl",), ("data","descUrl"), ("pageModule","descUrl"), ("actionModule","descUrl")
        ]:
            val = deep_get(rp, *kp)
            if isinstance(val, str) and val.startswith("http"):
                try:
                    resp = await ctx.request.get(val, timeout=60_000)
                    if resp.ok:
                        html = await resp.text()
                        if html and len(html.strip()) > 30:
                            results.append(norm_html(html))
                except:
                    pass

    results += await fetch_iframe_desc(ctx, page)

    # Deduplicate
    def fp(s: str) -> str:
        t = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s)).strip().lower()
        return t[:4000]
    seen, uniq = set(), []
    for h in results:
        f = fp(h)
        if f and f not in seen:
            seen.add(f)
            uniq.append(h)
    return uniq

def html_to_md(html_text: str) -> str:
    try:
        return md(html_text, strip=['style','script'])
    except:
        return "_(conversion to markdown failed, keeping HTML only)_"

async def fetch_once(url: str, outdir: str = "exports"):
    url, pid = normalize_and_extract_id(url)
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        ctx = await browser.new_context(
            locale="en-US",
            user_agent=("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"),
        )
        page = await ctx.new_page()
        await page.goto(url, wait_until="domcontentloaded", timeout=120_000)
        await page.wait_for_timeout(900)
        for y in (300, 1200, 2400):
            try:
                await page.evaluate(f"window.scrollTo(0,{y});")
                await page.wait_for_timeout(250)
            except:
                break

        parts = await extract_all_descriptions(ctx, page, mobile=False)

        # If we didn't get multiple chunks, try mobile too
        if len(parts) < 2:
            mobile_url = re.sub(r"^https?://www\.", "https://m.", url).split("?")[0]
            if not mobile_url.endswith(".html"):
                mobile_url += ".html"
            try:
                mpage = await ctx.new_page()
                await mpage.goto(mobile_url, wait_until="domcontentloaded", timeout=120_000)
                await mpage.wait_for_timeout(600)
                parts += await extract_all_descriptions(ctx, mpage, mobile=True)
                await mpage.close()
            except:
                pass

        # Final de-dupe across sources
        seen, uniq = set(), []
        for h in parts:
            k = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h)).strip().lower()
            if k and k not in seen:
                seen.add(k)
                uniq.append(h)

        if not pid:
            # fallback: extract digits again from final URL
            pid = "".join(re.findall(r"\d", url))[-16:] or "aliexpress-item"

        full_md = ""
        if uniq:
            full_md = (DIVIDER_MD).join(html_to_md(h) for h in uniq)
        else:
            full_md = "_(No description section found)_"

        Path(outdir).mkdir(parents=True, exist_ok=True)
        out_path = Path(outdir) / f"{pid}.md"

        # Add a tiny header with source URL for traceability
        header = f"> Source: {url}\n\n"
        out_path.write_text(header + full_md, encoding="utf-8")

        print(f"Saved: {out_path}")


        print("-" * 10)

        print(full_md)
        await browser.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/aliexpress_export.py <product_url> [outdir]")
        sys.exit(1)
    url = sys.argv[1]
    outdir = sys.argv[2] if len(sys.argv) > 2 else "exports"
    asyncio.run(fetch_once(url, outdir))

