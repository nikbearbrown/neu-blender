# NEU Blender: a 3D model of the Northeastern University Boston campus

**What this is:** a long-running project to build every Northeastern building in Blender, starting with rough blocks and adding detail over time.

**Why:** a campus model lets planners see a building before the university spends millions on it, and gives us the base for virtual campus tours, walkthrough films and games set on campus.

**Where it stands (October 2026):** data gathering. No model exists yet. We have a table of every Boston-campus building (levels above and below ground, floor area, year built, use), a folder-by-building inventory of the University Archives' photograph collection, and a plan for how to turn them into blocks. The two hardest buildings, ISEC and EXP, are waiting on drawings from their architect, Payette.

## How the project is organised
| Folder | What is in it |
|---|---|
| `data/tables/` | Facts as spreadsheets: the 2012 Facilities Data Matrix, the Archives inventory. Committed. |
| `data/sources/` | The original PDFs. Local only; `data/SOURCES.md` says where to get each one. |
| `data/plans/` | Drawings from architects and Facilities, when we get them. Local only unless cleared. |
| `reference-images/` | Photographs for modelling. Local only; `IMAGE-LOG.csv` records provenance. |
| `buildings/` | One folder per building with its notes, measurements and status. Start at `buildings/README.md`. |
| `blender/` | Blender scenes and the scripts that generate them. |
| `scripts/` | Data-processing scripts. |
| `ROADMAP.md` | The plan, in order. |

## Honesty rule
Every number in a model has a source, and anything estimated (floor heights, footprints scaled from a drawing) is marked as estimated. Numbers from 2012 or from a 2013 proposal are not the built building.

## Rights
Images and drawings belong to their owners (Northeastern University, Payette, photographers). This repository holds our tables, scripts and models, not their files. Licence for our own work: not yet chosen.
