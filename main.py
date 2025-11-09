# main.py — mkdocs-macros (relative links, no dup paths)
from pathlib import Path
import re

def define_env(env):
    @env.macro
    def children(exclude=('index.md',), recursive=False):
        page = env.variables["page"]
        docs_dir = Path(env.conf["docs_dir"])

        # e.g. "components/DC-DC Step Down/index.md"
        rel_uri = page.file.src_uri
        folder_rel = Path(rel_uri).parent
        folder_abs = docs_dir / folder_rel

        # Collect .md files
        md_paths = folder_abs.rglob("*.md") if recursive else folder_abs.glob("*.md")
        md_paths = [p for p in md_paths if p.name not in exclude and (recursive or p.parent == folder_abs)]

        items = []
        for p in md_paths:
            # Prefer YAML title -> first H1 -> filename
            text = p.read_text(encoding="utf-8", errors="ignore")
            m = re.search(r'(?m)^title:\s*(.+)$', text)
            if m:
                title = m.group(1).strip()
            else:
                h1 = re.search(r'(?m)^#\s+(.+)$', text)
                title = h1.group(1).strip() if h1 else p.stem.replace("-", " ")

            # Build a link RELATIVE TO THE CURRENT FOLDER (critical!)
            rel_to_folder = p.relative_to(folder_abs).as_posix()  # e.g. "PS001.md" or "sub/PS010.md"
            url = rel_to_folder if rel_to_folder.endswith(".md") else rel_to_folder + ".md"

            items.append((title, url))

        # Sort by title
        items.sort(key=lambda t: t[0].lower())

        # Emit simple bullet list (works everywhere)
        return "\n".join(f"- [{t}]({u})" for t, u in items)

