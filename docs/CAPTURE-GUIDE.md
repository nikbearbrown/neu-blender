# Capture guide: photographing a Northeastern building with a GoPro

**What this is:** instructions for anyone borrowing the GoPro to photograph a campus building for the Blender model.
**Why:** the archive photos are old and show people more than buildings. Fresh photos of every face of a building, taken the same way each time, are the fastest way to get facades, materials and window layouts right.
**What you will bring back:** a folder of photos for one building, plus a one-page notes sheet (`docs/capture-notes-template.md`). Allow 15-30 minutes for a small building, an hour for a large one.

## Before you go
- Pick the building from the list Bear gives you. We work one at a time, as each is modelled.
- Charge the camera, clear the card, bring a spare battery.
- Choose a dry, overcast day if you can. Bright sun and deep shadow are hard to fix later. Early morning is good for quiet sidewalks.
- Bring a phone (for notes) and, if you have one, a tape measure.

## Camera settings (check the model's menus; names vary)
| Setting | Use | Why |
|---|---|---|
| Mode | Photo, or Time Lapse Photo at 1 to 2 second interval while you walk | Sharper than video frames |
| Lens | Narrowest / "Linear" (not SuperView, not Wide) | Wide lenses bend straight building edges |
| Resolution | The highest photo resolution | More detail for textures |
| Horizon level | On, if offered | Keeps verticals upright |
| Date/time and GPS | On | Lets us place photos on the map |

## What to shoot (for each building)
1. **Sign or address first.** One photo of the building name or number, so the folder is identifiable.
2. **Every face, square on.** Walk the whole length of each side along the sidewalk, keeping the camera level and as square to the wall as you can. Keep the whole facade in frame where possible, even if it means crossing the street.
3. **Corners.** From each corner, one shot that shows two faces at once.
4. **Entrances.** One wide shot and one close shot of each main entrance, including doors and any canopy.
5. **Rooflines.** If you can see the top of the building from a safe distance, shoot it. We want to know: flat roof, pitched roof, penthouse or mechanical box.
6. **Materials, close up.** Brick, concrete, metal, glass, trim. Hold the camera 1 metre from the wall, level, and shoot a patch about 2 metres wide. If you can, put a tape measure or a known object, like a door, in the picture for scale.
7. **Floors and windows.** Photograph a section of wall in which you can count the rows of windows. Write down the number of floors.
8. **Context.** Where the building sits relative to its neighbours, trees, steps, ramps and the sidewalk.

## Do not
- Go inside restricted areas or onto roofs. Photograph from public sidewalks and paths only.
- Block doorways or stop people. If someone asks you to stop, stop and thank them.
- Take close photos of people's faces or number plates. If they end up in a shot, take another.
- Fly drones. Boston has strict rules and we do not use them.
- Use anything from the photos beyond this project without checking with Bear.

## File names and where they go
Name each photo `<building-code>_<face>_<NN>.jpg`, for example `DG_south_03.jpg`. The building code is in `data/tables/facilities_matrix_2012.csv` (Dodge Hall is `DG`, Richards Hall is `RI`). Faces are `north`, `south`, `east`, `west`, or `corner-ne` and so on, as best you can tell. Put the files in a folder named for the building and give it to Bear (shared drive or USB, decided per project).

Fill in `docs/capture-notes-template.md`: number of floors, roof type, materials, entrances, anything odd (construction, scaffolding, trees blocking one side). Save it with the photos.

## For Bear (after receiving photos)
1. Move the files into `reference-images/<building-code>/`. They stay out of git.
2. Add a row for each (or a group) to `reference-images/IMAGE-LOG.csv`, source "own photo", rights "own".
3. Copy the notes sheet into `buildings/<code>/` and update that building's README.
