#!/usr/bin/env python3
"""Build a photo index (metadata only, no image files) for each campus building from the
Northeastern Digital Repository Service (DRS), collection neu:6012 = the digitized part of
the Northeastern University photograph collection (A103).

For every Boston-campus building in data/tables/facilities_matrix_2012.csv it runs a public
search of that collection and records each hit's id, title, abstract and a guess at what it
shows (a building view, a drawing/plan, or something else, usually people).

Usage:
  python3 -I scripts/index_drs.py data/tables/facilities_matrix_2012.csv data/tables/drs_photo_index.csv [--only "Dodge Hall" ...]

Standard library only. Waits 1 s between requests. Titles are search-hit text, not rights
statements: check each item's rights on its DRS page before saving or reusing an image.
"""
import csv, html, re, sys, time, urllib.parse, urllib.request

BASE = "https://repository.library.northeastern.edu"
COLLECTION = "neu:6012"
UA = "neu-blender-index/0.1 (research index; contact via github.com/nikbearbrown/neu-blender)"
VIEW = re.compile(r"exterior|front of|view of|facade|entrance|aerial|construction|building|rear of|side of|corner", re.I)
DRAWING = re.compile(r"floor plan|architectural|drawing|blueprint|rendering|elevation|site plan|\bmodel\b|master plan|proposed", re.I)
ITEM_START = "<article class='drs-item'"
TITLE = re.compile(r"<h4 class='drs-item-title'>.*?<a href='[^']*'>(.*?)</a>", re.S)
ABSTRACT = re.compile(r"<dd class='drs-item-abstract'[^>]*>(.*?)</dd>", re.S)
TOTAL = re.compile(r"Displaying (\d+) to (\d+) of (\d+)")


def clean(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<!--.*?-->|<[^>]+>", " ", s, flags=re.S))).strip()


def fetch(q, page):
    url = f"{BASE}/collections/{COLLECTION}?" + urllib.parse.urlencode(
        {"q": q, "per_page": 100, "rows": 100, "page": page, "sort": "title_ssi asc"})
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=40) as r:
        return r.read().decode("utf-8", "replace")


def search_term(name):
    name = re.sub(r"\(.*?\)", "", name)           # drop parentheticals
    name = re.sub(r"\s+-\s+.*$", "", name).strip()  # "International Village - Residence" -> name
    return f'"{name}"' if " " in name else name


def kind(text):
    if DRAWING.search(text):
        return "drawing"
    if VIEW.search(text):
        return "view"
    return "other"


def main(matrix, out, only):
    with open(matrix) as f:
        rows = [r for r in csv.DictReader(f) if r["source_pdf_page"] in ("383", "384", "385")]
    if only:
        rows = [r for r in rows if r["name"] in only]
    result = []
    for r in rows:
        term = search_term(r["name"])
        plain = term.strip('"').lower()
        page, ids = 1, set()
        while True:
            try:
                body = fetch(term, page)
            except Exception as e:  # keep going; note the failure
                print("FAIL", r["name"], e); break
            blocks = body.split(ITEM_START)[1:]
            new = 0
            for b in blocks:
                m = re.search(r"data-drsitem='(neu:[^']+)'", b)
                if not m or m.group(1) in ids:
                    continue
                iid = m.group(1); ids.add(iid); new += 1
                t = clean(TITLE.search(b).group(1)) if TITLE.search(b) else ""
                a = clean(ABSTRACT.search(b).group(1)) if ABSTRACT.search(b) else ""
                result.append(dict(building_code=r["code"], building_name=r["name"], query=term,
                                   item_id=iid, title=t, abstract=a, kind=kind(t + " " + a),
                                   name_in_text=str(plain in (t + " " + a).lower()),
                                   url=f"{BASE}/files/{iid}"))
            m = TOTAL.search(body)
            last, total = (int(m.group(2)), int(m.group(3))) if m else (0, 0)
            print(f"{r['name']!r}: {len(ids)} items (shown to {last} of {total})")
            if not new or last >= total or page >= 8:
                break
            page += 1
            time.sleep(1)
        time.sleep(1)
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(result[0].keys()))
        w.writeheader(); w.writerows(result)
    print(len(result), "rows ->", out)


if __name__ == "__main__":
    args = sys.argv[1:]
    only = []
    if "--only" in args:
        i = args.index("--only"); only = args[i + 1:]; args = args[:i]
    main(args[0], args[1], only)
