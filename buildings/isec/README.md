# ISEC — Interdisciplinary Science and Engineering Complex (data gathered so far)

**What this is:** every fact about the Interdisciplinary Science and Engineering Complex layout that the three sources you gave state outright, plus a list of what they do NOT give. **Found:** program, a room-numbering scheme, a handful of named rooms with floors, and the building's total area. **Not found:** any dimension, footprint, floor count, or plan geometry. The sources give enough for a labelled massing diagram, not a scaled model. Everything below is tagged with its source.

Sources (kept locally in `data/sources/`, not committed; see `data/SOURCES.md`):
- **P** = Payette project page, https://www.payette.com/project/northeasternisec/
- **A** = Acentech project page, https://www.acentech.com/project/northeastern-university-isec/
- **G** = ISEC Building Use Guidelines 2024 (PDF, 9 pp.), `data/sources/ISEC-Guidelines-2024-1.pdf`

Note: the pages say "Interdisciplinary" (P, G) and "Integrated" (A body text) Science and Engineering Complex. Same building.

## Whole building
| Fact | Value | Src |
|---|---|---|
| Gross area | 234,000 GSF | P, A |
| Completed | 2016 | P |
| Architect | Payette | A |
| Site | Northeastern's southern border, linking Roxbury and Fenway; sloping ground plane | P |
| Neighbours | rail lines (MBTA + Amtrak) close by; PedX pedestrian bridge / track crossing; the EXP building shares operations ("ISEC/EXP Operations Team") | P, A, G |
| Skin | curved bronze solar veil/fins shading the office pod; glass office pod; layered weathering-steel bridge guard panels | P |
| Interior concept | clear glass walls instead of solid partitions; clear glass sidelight at every office | G |
| Research groups | "over 100" | G |
| Energy | LEED-NC 3 Gold, EUI 91 kBtu/SF | P |
| Hours | entrances Mon-Fri 6am-10pm, Sat 6am-6pm, closed Sun | G |

## Vertical organisation
- **Basement exists** (battery bin and service/freight elevator are there) — G.
- **Level numbering = first digit of the room number** (auditorium 102, atrium 101, classrooms 136/138/140/142 are all Level 1). The "X01, X05, X32" conference rooms repeat "on most of the floors" — G. (Inference from the numbering, not stated outright.)
- **Atrium: six stories, daylight-filled**, surrounded by collaboration spaces; acts as the mixing chamber for the cascade air system — P.
- Payette shows plans for Site, Level One, Level Two, Level Four (images only; contents not in text) — P.
- **Total floor count and building height: not stated in any source.**

## Named spaces
| Space | Level / room | Notes | Src |
|---|---|---|---|
| Atrium (lobby, event space) | 101, Level 1, rising 6 stories | only bookable common space; café is separate and not part of it | G, P |
| Auditorium | 102, Level 1 | central plant room is directly beneath it (sound/vibration isolated) | G, A |
| Classrooms | 136, 138, 140, 142, Level 1 | | G |
| Café | Level 1 (lobby area) | separate from event space | G |
| Catering kitchen | at atrium | atrium events only | G |
| Bike room | first floor | | G |
| Central plant room | below the auditorium (basement/low level) | "major," large equipment | A |
| Loading dock + freight elevator | dock at grade; freight elevator reaches the basement and every floor | each floor has a recycling hamper near the freight elevator | G |
| Battery bin | basement, near service/freight elevator | | G |
| Conference rooms | X05 (seats 5), X01 (seats 12), X32 (12 at table + 6 second row) | on most floors | G |
| Kitchen / lounge / balcony | one set on each floor | | G |
| Shower rooms | location not stated | card access | G |
| Office pod | glass volume, bronze veil | floor not stated | P |
| Write-up spaces | sit between offices and labs, glass walls to the labs | | G |
| Labs | Biology, Bioengineering, Computational Biology, Genomics, High-Throughput Screening, Imaging, Materials Characterization, Metabolomics, Teaching | "layered organization"; floors not stated | P |
| Sensitive labs | vibration-sensitive, located to limit rail-induced vibration | location not stated | A |

## Not in any source (needed before a scaled Blender model)
1. Footprint dimensions, floor-to-floor heights, total height, number of floors.
2. Plan geometry: where the atrium sits relative to the lab wings, column grid, core/stair/elevator positions.
3. Which labs/departments are on which level; where the office pod sits.
4. Orientation (compass bearing) and the slope of the site.
5. Exact location of the track crossing / PedX relative to the building.

## Data still to find
- Payette Level 1/2/4 plan images (download the images from the project page; I can vectorise or trace them).
- Northeastern campus map / fire-evacuation plans for ISEC (usually posted per floor), room-number floor plans from facilities.northeastern.edu.
- Boston Planning/BPDA filing for ISEC (gives height, footprint, floor count, setbacks).
- Boston city GIS / MassGIS building footprint and LiDAR for the 360 Huntington/Columbus Place parcel (real footprint + roof height).
- Any building section drawing showing the six-story atrium.

## Proposed modelling plan once data arrives
Put measured numbers in a `controls.json` with a source for each, generate the Blender scene from it, and mark anything estimated as `estimated` rather than blending it in. Until footprint/height exist, a model would be a diagram, not a measured model.

## Neighbour: EXP (added 2026-10-18)
Source: Payette, https://www.payette.com/project/northeasternexp/
- 357,000 GSF, completed 2023, LEED Platinum, EUI 81 kBtu/SF.
- Program: research labs, robotics, makerspace. Pinwheel plan defines four research clusters with collaboration space between them; lab modules in high/low-energy groupings; transparent perimeter zone of writing desks and offices.
- Level 8 (implied by "8th floor"): public Sky Garden, event spaces, Faculty Club, Executive Administration. Total floor count and height not stated.
- Exterior: folded stainless-steel ribbons pinwheeling around the building; scale chosen to echo ISEC's vertical shading.
- Called "the final piece" of a precinct of "over 600,000 square feet" (ISEC + EXP + PedX crossing). How EXP physically connects to PedX is not stated.
- Plans shown on the page: Levels 1, 2, 6, 8.

## From the 2013 Northeastern IMP (added 2026-10-18)
Source: `data/sources/2013_Northeastern_IMP.pdf` (447 pp., 186 MB, local only). Pages 82 and 84 are the useful ones. **This is a 2013 PLAN, not the as-built building.** There the building is called ISEB.
- Site: 795 Columbus Avenue ("Columbus Lot"), 2.7 acres, was a surface parking lot (482 spaces). (p84-85)
- Proposed ISEB: **6 stories, ~220,000 GSF** (as built: 234,000 GSF per Payette). Est. cost $150-175M. (p84-85)
- Other lot buildings proposed alongside: Academic/Mixed Use 1 (8-14 stories, 240-270k GSF) and Mixed Use 2 (5-7 stories, 150-160k GSF). EXP later took the place of one of these. Total lot 550-650k GSF. (p84)
- **Fig 7-2 (p84)** has a site plan at **"1 in = 100 ft"** showing the ISEB footprint, Columbus Ave, the Ruggles MBTA tracks, Cunard St, Coventry St and St Cyprians Place, plus a site section A-A (not to scale) and three massing views. Page is 17x11 in, so 72 PDF points = 100 ft. A rough measure of the ISEB shape gives about 300 ft x 120 ft; that times 6 floors is about 216,000 sq ft, which agrees with the stated 220,000 GSF. Treat as a sanity check, not a measurement. The built footprint may differ.
- Site plan spot elevations (e.g. +16.0, +18.0, +27.8, +31.0, +32.0) appear in the vector art; units/datum not yet identified.
- **Fig 7-1 (p82)** is an illustrative plan of the whole campus with every existing building footprint (pink) and proposed ones (red). This is a usable basemap for "every building at NEU."
- Pedestrian crossing: two new crossings plus an elevated promenade over the tracks at the Columbus Lot, sloped for accessibility, landing at the Science Quad and near Egan. (p72) This became PedX.
- Off-street loading for ISEB and all new buildings. (p210)
