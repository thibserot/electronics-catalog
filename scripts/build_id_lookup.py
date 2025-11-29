#!/usr/bin/env python3
"""
build_id_lookup.py
------------------
Reads docs/components/stickers/id_registry.yaml and generates
docs/id-lookup/index.md with a sortable table of all component IDs,
names, and links to their pages.

This helps quickly find components that are in subdirectories.

Run this after generate_id_registry.py.
"""

from pathlib import Path
import sys, yaml, datetime

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SRC  = DOCS / "components" / "stickers" / "id_registry.yaml"
OUTD = DOCS / "id-lookup"
OUTD.mkdir(parents=True, exist_ok=True)
OUT  = OUTD / "index.md"

def main():
    if not SRC.exists():
        print(f"[error] Missing {SRC}. Run generate_id_registry.py first.", file=sys.stderr)
        sys.exit(1)

    data = yaml.safe_load(SRC.read_text(encoding="utf-8")) or {}
    ids_list = data.get("ids", [])
    gen_at   = data.get("generated_at", "")

    # Build ID lookup table
    table_lines = []
    table_lines.append("| ID | Name | Category | Link |")
    table_lines.append("|---|---|---|---|")

    # Sort by ID alphabetically
    for entry in sorted(ids_list, key=lambda x: x.get("id", "")):
        comp_id = entry.get("id", "")
        name = entry.get("name", "")
        category = entry.get("category", "")
        url = entry.get("url", "")

        # Create a relative link from the source path
        # The id-lookup page is at docs/id-lookup/index.md
        # Component pages are at docs/components/...
        # So we need ../components/...md relative links
        source = entry.get("source", "")
        if source:
            # Convert source path to relative link with .md extension
            # source format: components/AC001.md or components/Motor-Drivers/index.md
            link = f"[{comp_id}](../{source})"
        else:
            link = comp_id

        table_lines.append(f"| `{comp_id}` | {name} | `{category}` | {link} |")

    content = f"""---
title: Component ID Lookup
hide:
  - toc
---

# Component ID Lookup

_This page is generated from `components/stickers/id_registry.yaml`._
**Generated:** {gen_at or datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z"}

Quick lookup table for all component IDs. Use this to find components in subdirectories.

{"\n".join(table_lines)}

"""
    OUT.write_text(content, encoding="utf-8")
    print(f"[ok] Wrote {OUT.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
