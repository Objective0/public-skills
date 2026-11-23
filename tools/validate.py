#!/usr/bin/env python3
"""Checks the library's format and looks for anything unsafe. Run before opening a pull request:

  python3 tools/validate.py

Errors fail the check. Warnings are for the reviewer, and don't fail it.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")
NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
TEXT = {".md", ".txt", ".csv", ".json", ".yaml", ".yml"}
IMAGES = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}
UNSAFE = [
    (re.compile(r"ignore (all )?(previous|prior|above) instructions", re.I), "tries to override the agent's instructions"),
    (re.compile(r"(sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|xox[bap]-[A-Za-z0-9-]{10,}|AKIA[0-9A-Z]{16})"), "looks like a key or token"),
    (re.compile(r"(webhook\.site|requestbin|pipedream\.net|ngrok\.io)", re.I), "links to a service that collects data"),
    (re.compile(r"\b(curl|wget)\b[^\n]*(-d|--data|-X\s*POST)", re.I), "sends data to a URL"),
]

errors, warnings = [], []


def front(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, text
    meta, key = {}, None
    for line in m.group(1).splitlines():
        if re.match(r"^[A-Za-z][\w-]*:", line):
            key, val = line.split(":", 1)
            meta[key] = val.strip()
        elif key:
            meta[key] = (meta[key] + " " + line.strip()).strip()
    return meta, text[m.end():]


def main():
    if not os.path.isdir(SKILLS):
        sys.exit("No skills/ folder.")
    seen = {}
    for author in sorted(os.listdir(SKILLS)):
        adir = os.path.join(SKILLS, author)
        if not os.path.isdir(adir):
            continue
        if not NAME.match(author):
            errors.append(f"skills/{author}: author folder must be lowercase words joined by hyphens")
        apath = os.path.join(adir, "author.md")
        if not os.path.isfile(apath):
            errors.append(f"skills/{author}: no author.md")
        else:
            meta, _ = front(apath)
            if not meta or not meta.get("name"):
                errors.append(f"skills/{author}/author.md: needs front matter with a name")
        for skill in sorted(os.listdir(adir)):
            sdir = os.path.join(adir, skill)
            if not os.path.isdir(sdir):
                continue
            where = f"skills/{author}/{skill}"
            if not NAME.match(skill) or len(skill) > 64:
                errors.append(f"{where}: folder name must be lowercase words joined by hyphens, at most 64 characters")
            if skill in seen:
                errors.append(f"{where}: the name is already used by {seen[skill]}")
            seen[skill] = where
            spath = os.path.join(sdir, "SKILL.md")
            if not os.path.isfile(spath):
                errors.append(f"{where}: no SKILL.md")
                continue
            meta, body = front(spath)
            if not meta:
                errors.append(f"{where}/SKILL.md: needs front matter with name and description")
                continue
            if meta.get("name") != skill:
                errors.append(f"{where}/SKILL.md: name must match the folder ({skill})")
            desc = meta.get("description", "").strip('|>" ')
            if not desc:
                errors.append(f"{where}/SKILL.md: needs a description")
            elif len(desc) > 1024:
                errors.append(f"{where}/SKILL.md: description is {len(desc)} characters; the most is 1,024")
            elif len(desc) > 200:
                warnings.append(f"{where}/SKILL.md: description is {len(desc)} characters; Claude's upload asks for 200 or fewer")
            if "## What good looks like" not in body:
                warnings.append(f"{where}/SKILL.md: no '## What good looks like' section")
            if body.count("\n") > 500:
                warnings.append(f"{where}/SKILL.md: over 500 lines; move depth into references/")
            for dirpath, _, files in os.walk(sdir):
                for f in files:
                    p = os.path.join(dirpath, f)
                    rel = os.path.relpath(p, ROOT)
                    ext = os.path.splitext(f)[1].lower()
                    if ext not in TEXT | IMAGES:
                        errors.append(f"{rel}: only text and image files are allowed in a skill")
                        continue
                    if ext in TEXT:
                        content = open(p, encoding="utf-8", errors="replace").read()
                        for pat, why in UNSAFE:
                            if pat.search(content):
                                errors.append(f"{rel}: {why}")
    for w in warnings:
        print("warning:", w)
    for e in errors:
        print("error:", e)
    print(f"{len(seen)} skills checked: {len(errors)} errors, {len(warnings)} warnings")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
