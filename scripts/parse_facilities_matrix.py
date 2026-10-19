#!/usr/bin/env python3
"""Parse the Facilities Data Matrix (Appendix B, 2013 Northeastern IMP, PDF pp. 383-386)
into data/tables/facilities_matrix_2012.csv.

Reads text spans with their positions and rebuilds table rows by y-coordinate, because the
PDF's plain-text order scrambles some columns.

Usage: python3 -I scripts/parse_facilities_matrix.py data/sources/2013_Northeastern_IMP.pdf data/tables/facilities_matrix_2012.csv
Needs PyMuPDF (pip install pymupdf).
"""
import csv, re, sys
import fitz

PAGES = (383, 384, 385, 386)
YEAR = re.compile(r"^(\d{4}|Unknown|NU Built|c ?\d{4}|\d{4}[-\s].*)$")
GSF = re.compile(r"^[\d,]+ sf$")
INT = re.compile(r"^\d+$")
NOISE = re.compile(r"(^\d+ buildings?$|acres|^Sub-?total|^Total|^[\d,.]+( sf)?$|^Page \d of \d$)", re.I)
HEADER = {"Northeastern University  -  Facilities Data Matrix", "Issue Date 10-01-12", "Building Name",
          "Code", "Official Street Address", "Year Built", "Year Acquired", "Year Major", "Renovation",
          "Renovaiton", "Below", "Above", "Penthouse", "Levels", "Gross SF", "Owned or Leased",
          "Primary Building Use"}


def page_rows(page):
    spans = []
    for b in page.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            for s in l["spans"]:
                t = s["text"].strip()
                if t:  # visual coordinates (the matrix pages are rotated)
                    pt = fitz.Point((s["bbox"][0] + s["bbox"][2]) / 2, (s["bbox"][1] + s["bbox"][3]) / 2) * page.rotation_matrix
                    spans.append((pt.y, pt.x, t))
    spans.sort()
    rows, cur, y = [], [], None
    for yc, x, t in spans:
        if y is not None and abs(yc - y) > 3:
            rows.append(sorted(cur)); cur = []
        cur.append((x, t)); y = yc
    if cur:
        rows.append(sorted(cur))
    return [[t for _, t in r] for r in rows]


def main(pdf, out):
    doc = fitz.open(pdf)
    rows, section = [], ""
    for pno in PAGES:
        for cells in page_rows(doc[pno - 1]):
            if all(c in HEADER for c in cells):
                continue
            if len(cells) >= 8 and GSF.match(cells[-3]) and cells[-2] in ("Owned", "Leased"):
                gsf, own, use = cells[-3], cells[-2], cells[-1]
                ints = cells[-6:-3]
                if not all(INT.match(i) for i in ints):
                    continue  # subtotal rows
                below, above, pent = map(int, ints)
                rest = cells[:-6]
                years = []
                while len(rest) > 3 and YEAR.match(rest[-1]):
                    years.insert(0, rest.pop())
                if len(rest) < 3:
                    continue
                name, code, addr = rest[:3]
                rows.append(dict(section=section, name=name, code=code, address=addr,
                                 year_built=years[0] if years else "",
                                 year_other="; ".join(years[1:]),
                                 below=below, above=above, penthouse=pent,
                                 gsf=int(gsf.split()[0].replace(",", "")),
                                 ownership=own, use=use, source_pdf_page=pno,
                                 needs_check="above=0 with below>0" if above == 0 and below > 0 else ""))
            elif len(cells) == 1 and not NOISE.search(cells[0]):
                section = cells[0]
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    print(len(rows), "rows ->", out)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
