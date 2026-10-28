# REVIEW: Fire Claims Decoded series trailer

Render: `renders/fire-claims-decoded-series-trailer.mp4`, 1080x1920, 30 fps, 31.5 s,
H.264 + AAC, 22 MB.

## What it is

The loud version of the series explainer, made because the first one (blueprint
diagrams, `../claims-decoded-explainer`) read as too plain. Real-time fire behind
every shot, type that slams in on the beat, camera shake and flash frames on hits,
and an original trailer score.

| time | beat | on screen |
|---|---|---|
| 0-3 | hook | STOP. / THERE ARE 3 FIRE CAUSES / IN YOUR BUILDING. RIGHT NOW. |
| 3-9 | the 3 causes | 1 LOOSE WIRING · 2 GREASY KITCHEN DUCTS · 3 BLOCKED AISLES, each drawing ignites, whip to the next |
| 9-13 | the turn | YOU WALK PAST THEM EVERY DAY. / fire engulfs the frame: UNTIL ONE STARTS A FIRE. / FIRE CLAIM stamp |
| 13-19 | reveal | FIRE CLAIMS DECODED / I'M AN ENGINEER IN PROPERTY INSURANCE. / I SHOW YOU HOW FIRES REALLY START. |
| 19-24.5 | the promise | HOMES. SHOPS. RESTAURANTS. WAREHOUSES. FACTORIES. ONE OCCUPANCY AT A TIME. / HOW IT STARTS. / HOW TO STOP IT. (the fire dies) |
| 24.5-27.5 | the point | SO YOU NEVER HAVE TO MAKE THE CLAIM. |
| 27.5-31.5 | end card | FIRE CLAIMS DECODED · @parag_pethe1 · FOLLOW · 1 FIRE CAUSE EVERY REEL |

Hook: "Stop. There are 3 fire causes in your building right now." scored 84.4 STRONG
on `ig-reel/hookscore.py` (formula #2 Negative Command); the 6 s after it pay it off.

## Sound

- The score is original, synthesised by `tools/make_score.py` to the film's cue sheet:
  120 BPM, D minor, sub booms and a low brass blast on the hook, a taiko and bass
  groove under the causes, a riser into the engulf, the biggest hit on the title, a
  drop to near silence as the fire dies, a D major pad for the relief, a final hit on
  the end card.
- It was **measured, not heard**. Final file: -16.8 LUFS integrated, true peak
  -1.8 dBTP, no clipping. 13 of 18 cues have a strong onset within 5 ms of the picture.
- No outside music library was reachable from this environment (Hugging Face,
  HeyGen, Pixabay, Openverse and Freesound are blocked). To use a licensed track
  instead, replace `assets/audio/score.m4a` (or point `<audio id="music">` in
  `index.html` at the new file) and re-render. On Instagram, a track from its library
  can also be laid over the upload.

## Measured / looked at

- `hyperframes check`: passes. Kept: a GPU stall note from the software renderer
  (performance only) and "escaped container" during the whips (text is meant to be
  off-screen mid-whip).
- Frames read by eye at 27 moments across two passes; fixes made: cause drawings
  moved below their labels, three lines that touched the right edge resized,
  occupancy names held 0.4 s each.

## Weakest moment

The three cause drawings are line icons; they ignite and whip, but they are still
icons. With real photos or Gemini clips of a burnt socket, a greasy duct and a
blocked aisle, that section would hit harder. Swap them in the `#s2-art*` slots.

## Rebuilding

`python3 tools/build_scenes.py` regenerates `compositions/s1-s7.html`.
`python3 tools/make_score.py out.wav` (needs numpy, scipy, soundfile) regenerates the
score; then encode it with
`ffmpeg -i out.wav -af "volume=-0.3dB,alimiter=limit=0.56:level=false:attack=1:release=80" -c:a aac -b:a 256k assets/audio/score.m4a`.
The fire is a WebGL shader in `compositions/fire.html`; its shape over time is the
`KEYS` table at the top of that file.
