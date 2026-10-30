# REVIEW: Fire Claims Decoded explainer

Render: `renders/fire-claims-decoded-explainer.mp4`, 1080x1920, 30 fps, 31.8 s, H.264 + AAC.

## Creative calls

- Built storyline A, "Smaller than your thumb" (picked by Parag). Not built: B "Decoded"
  (claim files that unscramble) and C "One street, one take". Both are in `STORYLINES.md`.
- Look: engineering blueprint (flat #1F5F99, white line work, dashed hidden lines),
  chosen because the series is an engineer's view of fire causes.
- Accent changed from #FF6B1A to #FF9A3C: the first orange was 2.34:1 on the blue,
  under the 3:1 needed for the cause labels. #FF9A3C is 3.15:1.
- Every label comes from `.claude/instagram/voice.md` or the restaurant kitchen reel:
  loose wiring / annual electrical audit; grease in the duct / clean filters every 7
  days; blocked aisles / caged, segregated storage; overstocking / stock within
  permissible limits; "We are surrounded by fire causes every day. Most people never
  notice them."
- No presenter: there is no footage of Parag yet, so this is motion graphics only.

## What was measured, what was only looked at

- `hyperframes check`: passes. Kept one warning: a 2.92:1 contrast reading on S2 at
  8.83 s, which samples a word mid-way through its grey-to-white fade; it lands at
  full white a moment later.
- Snapshots at 16 moments plus re-checks of the fixes, read by eye.
- Audio measured, not heard: -16.9 LUFS integrated, true peak -4.8 dBTP, hits at
  the planned times.

## Sound

Sound effects only (Pixabay licence, `assets/sfx/CREDITS.md`). No music bed: no music
source was available in this environment (no HeyGen sign-in, no local music model).
To add one, drop a track in `assets/` and add an `<audio id="music">` to `index.html`
at about 0.14 volume.

## Weakest shot

S2 (the kitchen): the kadhai and flame sit small in the lower right and the left of
the frame is empty below the label. With more time: frame it tighter on the hood and
duct, and let the flame lick up into the hood.

## Environment notes

GSAP is loaded from `assets/vendor/` (copied from npm), because this environment
blocks the jsDelivr CDN.
