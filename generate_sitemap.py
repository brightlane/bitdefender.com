#!/usr/bin/env python3
"""
Auto Sitemap Generator
Scans all HTML files in the repo and rebuilds sitemap.xml automatically.
Run manually or via GitHub Actions on every push.
"""

import os
import glob
from datetime import date

# ── CONFIG ──────────────────────────────────────────────────────────────
BASE_URL = "https://brightlane.github.io/bitdefender.com"
TODAY    = date.today().isoformat()  # e.g. 2026-04-26

# Files to never include in sitemap
EXCLUDE = {
    "404.html",       # error page — no SEO value
}

# Priority and changefreq rules — matched by filename keyword
RULES = [
    {"match": "index",              "priority": "1.0", "changefreq": "weekly"},
    {"match": "bitdefender-review", "priority": "0.9", "changefreq": "weekly"},
    {"match": "bitdefender-coupon", "priority": "0.9", "changefreq": "daily"},
    {"match": "blog",               "priority": "0.8", "changefreq": "daily"},
]
DEFAULT = {"priority": "0.7", "changefreq": "weekly"}
# ────────────────────────────────────────────────────────────────────────


def get_rule(filename):
    for rule in RULES:
        if rule["match"] in filename:
            return rule
    return DEFAULT


def build_url_entry(filepath):
    filename = os.path.basename(filepath)

    if filename in EXCLUDE:
        return None

    # Build the public URL
    if filename == "index.html":
        loc = f"{BASE_URL}/"
    else:
        loc = f"{BASE_URL}/{filename}"

    rule = get_rule(filename)

    return f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>{rule['changefreq']}</changefreq>
    <priority>{rule['priority']}</priority>
  </url>"""


def generate_sitemap():
    # Find all HTML files in root of repo
    html_files = sorted(glob.glob("*.html"))

    entries = []
    skipped = []

    for filepath in html_files:
        entry = build_url_entry(filepath)
        if entry:
            entries.append(entry)
        else:
            skipped.append(os.path.basename(filepath))

    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
    sitemap += '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n\n'
    sitemap += "\n\n".join(entries)
    sitemap += "\n\n</urlset>"

    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap)

    print(f"✅ sitemap.xml updated — {TODAY}")
    print(f"   {len(entries)} pages included:")
    for filepath in html_files:
        name = os.path.basename(filepath)
        if name not in skipped:
            print(f"   + {name}")
    if skipped:
        print(f"   {len(skipped)} pages skipped: {', '.join(skipped)}")


if __name__ == "__main__":
    generate_sitemap()
