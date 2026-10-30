# REVIEW: Fire Claims Decoded series trailer

Render: `renders/fire-claims-decoded-series-trailer.mp4`, 1080x1920, 30 fps, 27.5 s,
H.264 + AAC, 22 MB.

## What it is

The loud version of the series explainer. A vivid background world per beat, real-time fire, type
that slams in on the beat, camera shake and flash frames on hits, and an original
trailer score. Cut v2 (2026-10-29) follows Parag's re-edit brief.

| time | beat | on screen |
|---|---|---|
| 0-3 | hook | STOP. / THERE ARE VARIOUS FIRE CAUSES AROUND YOU. / RIGHT NOW. |
| 3-10 | the turn | YOU WALK PAST THEM EVERY DAY. / fire engulfs the frame: UNTIL ONE INVISIBLE FIRE STARTS INTO GIANT VISIBLE ONE. / FIRE CLAIM stamp |
| 10-16 | reveal | FIRE CLAIMS DECODED / I WILL SHOW YOU HOW FIRES REALLY START IN VARIOUS OCCUPANCIES. |
| 16-20.6 | the promise | HOMES. SHOPS. RESTAURANTS. INDUSTRIES. ONE OCCUPANCY AT A TIME. / HOW IT STARTS. / HOW TO PREVENT IT. (the fire dies) |
| 20.6-23.5 | the point | SO YOU NEVER HAVE TO MAKE THE CLAIM. |
| 23.5-27.5 | end card | FIRE CLAIMS DECODED · @parag_pethe1 · FOLLOW · 1 FIRE CAUSE EVERY REEL |

Copy is Parag's, verbatim, except "THERE VARIOUS" corrected to "THERE ARE VARIOUS".
Cut v1 (31.5 s, with the three numbered causes) is in git history at b215bd8.

## Backgrounds (cut v2, second pass)

Each beat has its own vivid world, drawn in code (`compositions/bg.html`, built by
`tools/build_bg.py`), with the fire composited over it (the fire canvas is now
transparent):

| time | world |
|---|---|
| 0-3 | red alarm: siren beams sweep, a strobe on every slam, fire below |
| 3-5.5 | magenta-to-amber sunset over a market street: tangled wires, gas cylinders, cartons; hot spots pulse on the wires as the street drifts past |
| 5.5-10 | the fire takes the frame |
| 10-16 | thermal-camera view: purple, magenta and yellow heat over an electrical panel; the camera locks onto one white-hot breaker |
| 16-18 | one colour field per occupancy, cut on each word: teal house, magenta shop, amber kitchen, electric-blue factory |
| 18-19 | hot red as the fire surges |
| 19-20.6 | electric blue, sprinkler spray streaming down while the fire dies |
| 20.6-23.5 | safety green, slow light rays, a shield with a check mark drawn on |
| 23.5-27.5 | deep fire-red gradient under the end card |

Free stock libraries (Pexels, Unsplash, Wikimedia Commons, Pixabay, Flickr) are
blocked from this environment, and Parag chose not to spend ElevenLabs credits on
generated photos, so nothing here is a photograph. An unrun ElevenLabs flow with
photo prompts for every beat exists ("Fire Claims Decoded trailer backgrounds") if
photos are wanted later (about $1.80 at one image each).

## Sound

- The score is original, synthesised by `tools/make_score.py` to the film's cue sheet:
  120 BPM, D minor, sub booms and a low brass blast on the hook, a taiko and bass
  groove under the causes, a riser into the engulf, the biggest hit on the title, a
  drop to near silence as the fire dies, a D major pad for the relief, a final hit on
  the end card.
- Cut v2 keeps the same instruments and arrangement, with the hits moved to the new
  cue points.
- It was **measured, not heard**. Final file: -16.3 LUFS integrated, true peak
  -0.7 dBTP, no clipping. The renderer's mix came out at -19.1 LUFS, so the mastered
  score was muxed back into the MP4 (picture untouched). 9 of 14 cues have a strong
  onset within 5 ms; the rest are slow-attack booms placed exactly by the score code.
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

16-20.6 s is dense: four occupancy names, a line, then two more lines in 4.6 s.
Every line clears its reading floor, but it is the fastest stretch of the film.

## Rebuilding

`python3 tools/build_scenes.py` regenerates `compositions/s1.html` and `s3.html` to `s7.html`.
`python3 tools/make_score.py out.wav` (needs numpy, scipy, soundfile) regenerates the
score; then encode it with
`ffmpeg -i out.wav -af "volume=-1.0dB,alimiter=limit=0.5:level=false:attack=1:release=80" -c:a aac -b:a 256k assets/audio/score.m4a`.
After rendering, mux the score back in:
`ffmpeg -i render.mp4 -i assets/audio/score.m4a -map 0:v:0 -map 1:a:0 -c copy -shortest out.mp4`.
The fire is a WebGL shader in `compositions/fire.html`; its shape over time is the
`KEYS` table at the top of that file.
