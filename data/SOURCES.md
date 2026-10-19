# Data sources

**What this is:** the list of every outside document this project has used, where it came from, and a checksum so anyone can fetch the same file. The files themselves are not in the repo: they are large (the master plan is 186 MB, over GitHub's 100 MB file limit) and belong to their owners. Put your own copies in `data/sources/`.

| File (in `data/sources/`) | What it is | Where to get it | SHA-256 | Used for |
|---|---|---|---|---|
| `2013_Northeastern_IMP.pdf` | Northeastern Boston Campus Institutional Master Plan, 2013 (447 pp.) | City of Boston planning site: https://www.bostonplans.org/documents/institutional-planning/2013-northeastern-imp | `ae2bdbd1467f20e0e39184881ff7c6341bdc38be9119bff82ac1b9f80d72e38c` | Facilities Data Matrix (pp. 383-386), ISEC site plan (p. 84), campus footprint plan (p. 82) |
| `ISEC-Guidelines-2024-1.pdf` | ISEC Building Use Guidelines, 2024 (9 pp.) | https://isec.northeastern.edu/wp-content/uploads/2024/12/ISEC-Guidelines-2024-1.pdf | `c45d73e995a3b433a3182fbe69a4e3830e5229fbc3150a198f5bcaa661a020c7` | Room numbering, named ISEC spaces |

Web pages read (no local copy kept):
- Payette, ISEC: https://www.payette.com/project/northeasternisec/
- Payette, EXP: https://www.payette.com/project/northeasternexp/
- Acentech, ISEC: https://www.acentech.com/project/northeastern-university-isec/
- Northeastern Digital Repository Service, University photograph collection (A103), collection `neu:6012`: https://repository.library.northeastern.edu/collections/neu:6012
- Northeastern Archives, University Photograph collection (A103): https://archivesspace.library.northeastern.edu/repositories/2/resources/761

## Tables made from those sources (committed, in `data/tables/`)
| Table | Made by | Notes |
|---|---|---|
| `facilities_matrix_2012.csv` | `scripts/parse_facilities_matrix.py` | 127 rows: 98 Boston-campus buildings (47 academic, 37 residence, 10 athletic, 4 parking, matching the matrix's own subtotals) plus satellite sites. Figures are as of 1 Oct 2012. Rows with `needs_check` have levels that look wrong in the source (e.g. Cargill Hall shows 0 above grade). |
| `archives_A103_series11_physical_plant.csv` | pulled from the ArchivesSpace public tree | Folder-level inventory of Series 11 "Physical Plant": one folder per building, 251 rows including sub-folders. |
| `drs_photo_index.csv` | `scripts/index_drs.py` | Metadata only (item id, title, abstract, link) for DRS hits per Boston building. `kind` is a title-based guess; `name_in_text` says whether the building name appears in the hit's title or abstract. Check rights on each item page before saving an image. |
