# SPEC: Fire Claims Decoded explainer (storyline A, "Smaller than your thumb")

GOAL:    a stranger understands what Fire Claims Decoded is (an engineer in property
         insurance showing, one occupancy at a time, how fires start and how to prevent
         them) and taps Follow.
OUTPUT:  HyperFrames, 1080 x 1920 (9:16), 30 fps. Text only inside y 168-1330; below
         1330 drawing only. Left text margin 90 px.
TIME:    31.8 s x 30 = 954 frames. No music (no source available); sound effects only.
         S1 0-6.6 · S2 6.6-11.8 · S3 11.8-17.0 · S4 17.0-22.2 · S5 22.2-27.8 · S6 27.8-31.8
LOOK:    the medium is an engineering blueprint. Ground #1F5F99 flat, with a grid of
         white lines: 60 px at 7% and 300 px at 14%. Ink #F2F7FC, every structural line
         5 px, round caps. Hidden parts drawn as dashed lines (18/12), the drawing
         convention for what is behind a surface. Accent fire orange #FF9A3C, only on the
         cause in each scene (spark, grease, blocking pile, overstock) and on "DECODED".
         Secondary fill #174D7E (openings, the inside of things).
         Display: Oswald 700, cause labels 120 px, tracking 0; hook and lines Oswald 600
         76-80 px. Body: Roboto 500, 46-50 px. Left-aligned, never centred.
         No shadow, no grain, no vignette, no glow. Text sits on a 14 px halo of the
         ground colour so it reads over line work.
OBJECTS: a switchboard plate with two rocker switches and a 3-pin socket, wire and
         terminal behind it in dashed hidden line, the wire pulled loose from its
         screw; a commercial kitchen hood with filter slats and a rectangular duct
         rising to the roof, a kadhai on a burner; a warehouse aisle in one-point
         perspective, racks both sides, a pile of cartons in the middle of the aisle,
         a dashed route line that stops at the pile; a cracker shop seen through its
         rolled-up shutter, shelves of boxes, a dashed "PERMISSIBLE LIMIT" line with
         boxes above it and on the floor; a street of four building fronts (shop,
         restaurant, warehouse, cracker shop) with signboards.
MOTION:  camera = a wrapper per scene, transform-origin 0 0. Camera moves power2.inOut;
         zoom-through exits power3.in over 0.35 s with blur to 14 px; arrivals expo.out
         0.6-0.9 s from blur 12 px. Cause labels per word blur 6 px to 0 in 0.13 s,
         0.07 s apart; fix lines from 45% ink to full ink by word, 0.08 s apart.
         Exits 0.18 s blur-out. Landed text holds dead still.
SHOTS:
  S1 0-6.6    frame 0: hook "Most fire claims start with something smaller than your
              thumb." on screen over a shop switchboard. Camera pushes 1 -> 2.6 into
              the terminal behind the socket (0.4-3.2). 3.2 spark (orange) + click.
              Hook out 3.7. 3.9 "LOOSE WIRING" / "Fix: annual electrical audit", pop.
              Exit: zoom into spark, orange disc floods the frame. Whoosh.
  S2 6.6-11.8 orange disc shrinks into the kadhai flame. Camera tilts up 2.4 -> 1 to the
              hood and duct (0.5-2.0). Grease lines draw orange inside the duct (1.4-2.2).
              1.4 "GREASE IN THE DUCT" / "Fix: clean filters every 7 days", pop.
              Exit: zoom into the duct mouth. Whoosh.
  S3 11.8-17  the duct mouth becomes the aisle's far wall; camera pulls 5 -> 1. Route
              line draws toward the far wall and stops at the orange pile (0.8-1.6).
              1.3 "BLOCKED AISLES" / "Fix: caged, segregated storage", pop.
              Exit: zoom into the top carton. Whoosh.
  S4 17-22.2  arrive on an orange overstock box, pull 3 -> 1 to the whole shop.
              1.3 "OVERSTOCKING" / "Fix: stock within permissible limits", pop.
              Exit: pull back 1 -> 0.42 out of the shop front. Whoosh.
  S5 22.2-27.8 the shop front becomes the last of four buildings on a street; camera
              2.4 -> 1. Orange markers land on each building's cause (1.0-1.45).
              1.5 "We are surrounded by fire causes every day." 2.5 "Most people never
              notice them." Riser under the back half.
  S6 27.8-31.8 end card on the same ground: "FIRE CLAIMS" / "DECODED" wiped in, impact.
              "How fires start. How to prevent them." "@parag_pethe1"
              "Like · Follow · Comment". Holds 2.3 s.
BANNED:  dark navy void; glow, particles, flares; blue or purple gradients, glass cards;
         cream paper with serif and mono caps labels; pill chips and buttons; everything
         centred; fade-and-slide-up entrances; text moving while read; three cards in a
         row; docked corner logo; emoji in rendered text; AI-garbled or misspelled labels.
QA:      t=0 hook readable over the plate · t=3.4 spark at the terminal · t=5.5 S1 label ·
         t=6.7 orange flood into flame · t=10 hood + grease + label · t=15 aisle + pile ·
         t=20 shop + limit line · t=26.5 street + both lines · t=31 end card · every
         label spelled exactly as in this spec.
