"""Dependency-free sanity checks for the independently authored static portfolio."""
from pathlib import Path
from html.parser import HTMLParser
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PAGE = (ROOT / "index.html").read_text(encoding="utf-8")
JS = (ROOT / "main.js").read_text(encoding="utf-8")
CSS = (ROOT / "styles.css").read_text(encoding="utf-8")
README = (ROOT / "README.md").read_text(encoding="utf-8")


class PageInspector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.buttons = []
        self.external_assets = []
        self.sections = 0

    def handle_starttag(self, tag, attrs):
        props = dict(attrs)
        if "id" in props:
            self.ids.append(props["id"])
        if tag == "section":
            self.sections += 1
        if tag == "a":
            self.links.append(props)
        if tag == "button":
            self.buttons.append(props)
        if tag in ("script", "img") or (tag == "link" and props.get("rel") in ("stylesheet", "icon")):
            src = props.get("src") or props.get("href", "")
            if src.startswith(("https:", "http:", "//")):
                self.external_assets.append(src)


inspect = PageInspector()
inspect.feed(PAGE)
problems = []

def require(test, message):
    if not test:
        problems.append(message)

require(len(inspect.ids) == len(set(inspect.ids)), "Duplicate HTML ids")
require(all(x in inspect.ids for x in ("main", "top", "evidence", "work", "proposal", "principles", "next-step", "next-title", "next-description", "next-tag", "next-reason")), "Missing critical anchor or interaction IDs")
require(inspect.sections >= 4, "Critical content sections missing")
require(not inspect.external_assets, "Remote script, image, or stylesheet detected")
require("MIT License" in (ROOT / "LICENSE").read_text(encoding="utf-8"), "Site license missing")
for repo in ("janeq", "VideoOS", "jongfood"):
    require(f"https://github.com/tpeak5237/{repo}" in PAGE, f"Missing public {repo} evidence link")
for text in ("75", "181", "not yet proven", "not an existing AI agent", "PRIVATE SOURCE STAYS PRIVATE"):
    require(text.lower() in PAGE.lower(), f"Missing evidence or important limitation: {text}")
for path in ("wrong", "guess"):
    require(f"{path}: Object.freeze(" in JS, f"Missing deterministic branch: {path}")
    require(f'data-path="{path}"' in PAGE, f"Missing concept input: {path}")
for href in inspect.links:
    if href.get("target") == "_blank":
        require("noopener" in href.get("rel", "") and "noreferrer" in href.get("rel", ""), "External new-tab link missing safe rel")
for word in ("AIza", "sk-proj-", "ghp_", "BEGIN PRIVATE KEY", "supabase.co/rest/v1", "firebaseio.com"):
    require(word not in PAGE + CSS + JS, "Possible embedded credential or private service reference")
require("prefers-reduced-motion:reduce" in CSS, "Missing reduced-motion design")
require("aria-pressed" in PAGE and "aria-live" in PAGE and "activatePath" in JS, "Interaction is not accessible or not wired")
require("not a working ai agent" in README.lower(), "README must disclose proposal-only status")

for problem in problems:
    print("FAIL:", problem)
if problems:
    sys.exit(1)
print(f"PASS: {inspect.sections} sections, {len(inspect.links)} links, {len(inspect.buttons)} working UI controls, zero remote assets, evidence/claims/privacy checks")
