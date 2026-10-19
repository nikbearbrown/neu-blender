# Roadmap

**What this is:** the order of work, from a data table to a walkable campus. **Why in this order:** every level is useful on its own, so the model is never "not done" and can be used for tours or games at any stage.

## Level 0: campus blocks (all ~98 Boston buildings)
- Footprints: trace from the 2013 Master Plan illustrative plan (Fig. 7-1, p. 82), or extract the vector shapes from the PDF if it allows. Check against the City of Boston GIS footprints.
- Heights: levels above grade from `facilities_matrix_2012.csv` times an assumed floor-to-floor height (about 12-14 ft for residences, 14-16 ft for academic buildings, marked as estimated).
- Add since 2012: ISEC (2016), EXP (2023), PedX crossing, and anything else new. Each needs its own source.
- Terrain, Huntington Ave, the Orange Line cut and Ruggles tracks, the quads.

## Level 1: recognisable buildings
- Facade textures, window grids, roof shapes, entrances, for buildings players or visitors pass often.
- Source: reference photos (see `reference-images/README.md`) and drawings.

## Level 2: hero buildings
- Hand-built detail. Candidates: ISEC, EXP, Snell Library, Curry Student Center, plus wherever a game or tour needs it.
- Interiors only where a drawing exists.

## Data to chase
| Ask | Who | Why |
|---|---|---|
| ISEC/EXP section, plans, overall dimensions | Payette (contact form sent 2026-10-18) | The hardest buildings |
| Floor plans, record drawings | Northeastern Facilities | Real dimensions |
| Building heights and footprints | City of Boston planning filings (Article 80 library) and GIS | Cross-check |
| Architectural drawings, models, aerial photos | University Archives, A103 Series 11 (Architectural Drawings, Aerial Views, Master Plan) | Older buildings. Dated 1903-2003 so nothing for ISEC or EXP |
| Photos by building | Northeastern digital collections (Bear can log in) | Facade reference |

## Open decisions
- Licence for models and data tables (code is MIT).
- Whether to publish models, or only data and scripts, given the rights on source material.
