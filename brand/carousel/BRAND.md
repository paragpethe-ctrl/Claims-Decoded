# Fire Claims Decoded: carousel brand template

Use this for every carousel. The same look on every post makes your grid
recognisable at a glance, and every screenshot still carries your name.

## Canvas

- **Size:** 1080 x 1350 px (4:5), PNG.
- **Margins:** 96 px left and right, 72 px top, 64 px bottom. On the cover,
  keep all text at least 120 px from every edge so the grid crop never cuts it.
- **Slides:** 6 to 10. Never more than 10 for this series.

## Colours

| Role | Colour | Hex |
|---|---|---|
| Background | Near-black | `#0D0D0F` |
| Card / panel | Charcoal | `#17171B` |
| Brand, highlight, ✓ | Amber-gold | `#FFB300` |
| Danger, ✗, footer line | Red-orange | `#FF4D00` |
| Headlines | White | `#FFFFFF` |
| Body text | Soft grey | `#D6D6DA` |
| Counter, disclaimer | Muted grey | `#8E8E96` |

Background glow: a soft red-orange radial glow rising from the bottom edge
(about 40% strength), like embers. Nothing else decorates the slide.

These are the same colours as the Reel titles, so the Reels and carousels
look like one series.

## Fonts (all free, Google Fonts)

| Use | Font | Size |
|---|---|---|
| Cover headline | Anton, ALL CAPS | 150 px |
| Slide headline | Anton, ALL CAPS | 100 px |
| Big number / stat | Anton | 230–300 px |
| Body text | Inter Medium | 46 px (never below 32 px) |
| Labels, chip, footer | Inter Black / Bold | 32–34 px |
| Hindi text | Noto Sans Devanagari Bold | same sizes |

Highlight **one word** per headline in gold. Never more than one.

## Fixed parts (on every slide)

- **Top bar:** flame icon + "FIRE CLAIMS DECODED" in gold Anton (left), slide
  counter such as "3/9" (right), thin grey line under it.
- **Bottom bar:** 4 px red-orange line, "@fireclaimsdecoded" (left),
  "SWIPE →" in gold (right). The last slide drops "SWIPE".

## Series category (colour of the cover chip)

| Category | Chip colour |
|---|---|
| Fire safety | Gold `#FFB300` |
| Claim trigger | Orange `#FF8A00` |
| Claim rejection | Red-orange `#FF4D00` |
| Insurance fact | White |

Every cover chip also carries a running number: "CLAIM REJECTION · FILE #01".
The number turns the carousels into a collectable series.

## The 7 slide types

| Type | Use it for | Layout |
|---|---|---|
| `cover` | Slide 1 | Category chip + "DECODED" stamp, headline of 6 words or fewer, red-orange bar, 1-line promise |
| `stat` | Slide 2, the stake | Huge gold number ("1 DAY", "₹2.88 CR"), a label, 1 sentence |
| `point` | One idea per slide | Outlined gold number (01, 02…), headline, max 25 words |
| `split` | Covered vs not covered | Gold ✓ panel and red-orange ✗ panel |
| `myth` | Myth vs fact | Struck-out grey myth panel, gold fact panel |
| `recap` | The screenshot slide | "SAVE THIS" + gold checklist + disclaimer |
| `cta` | Last slide | 1 action headline, Save / Share / Follow rows, logo lockup, disclaimer |

The disclaimer "General information, not financial or legal advice. Check
your own policy." appears on the recap and CTA slides.

## Making a new carousel

1. Copy `decks/sample-5-claim-mistakes.json`, rename it, and change the text.
   Wrap the one gold word in [brackets].
2. Run `python3 build.py decks/<your-deck>.json`.
3. The PNGs appear in `out/<your-deck>/`, numbered in order, ready to upload.

To build the template in Canva instead, use the colours, fonts and sizes
above, and copy the sample PNGs in `out/sample-5-claim-mistakes/` as a guide.
