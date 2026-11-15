# Insurance awareness: two new pillars

The fire-cause reels earn attention. These two pillars turn that attention into action, and they are
where an insurance engineer's view is hardest to copy.

## Pillar 1: Why buy fire insurance (8 reels)

People don't buy cover because they think it's expensive, think it's only for factories, or think
someone else's policy already covers them. Each reel breaks one of those beliefs:

| belief | reel |
|---|---|
| "Nobody insures a home" | 01 Most homes have no cover (about 1% are insured) |
| "I rent, so I'm covered" | 02 Renting? Insure your things |
| "Claims get cut anyway" | 03 Bharat Griha Raksha (underinsurance doesn't apply) |
| "It's for big companies" | 04 Shop and small factory cover |
| "The bank already insured it" | 05 Check your bank's home policy |
| "Fire cover is only for fire" | 06 Storm and flood in a fire policy |
| "Insure what I paid for it" | 07 Insure the rebuild cost |
| "The form is a formality" | 08 The proposal form decides |

## Pillar 2: Lessons from rejected claims (8 reels)

Every reel follows the same pattern: what was decided, why, and what you'd do differently. They use
court decisions and standard policy wording only, never your own files or customers.

| why claims fail | reel |
|---|---|
| No records | 09 No stock register, no claim (Supreme Court, Sep 2026) |
| Records that look made up | 10 Fabricated records (NCDRC, 2025) |
| When the insured wins | 11 Suspicion isn't proof (NCDRC ordered 98 lakh paid) |
| Exclusions people miss | 12 The 30-day empty building rule, 13 Self-heating stock |
| Declarations | 14 False declarations |
| Admin mistakes | 15 A lapsed policy |
| The survey | 16 The surveyor's report |

Reel 11 matters for balance: it shows insurers also lose when they reject without proof. That keeps
the series fair to policyholders, not just a warning list.

## Rules for these pillars

- **Educate, don't sell.** No insurer names, no premium quotes presented as offers, no "buy from me".
  Product names used here are IRDAI's standard products, which every general insurer offers.
- **Say "check your policy wording".** Wordings differ; the reels say so.
- **Public decisions only.** Company names from judgments are left out of the reels even when public.
- **Add a line in the caption or bio:** "Educational content, not insurance advice."
- **Mix:** post 1 insurance reel after every 2 fire-cause reels.

## How each reel was built

Same as the other 51: hook scored with /ig-reel (94 to 100), beat sheet clean with a loop, /ig-human
pass on the script (73 to 82), caption linted with /ig-caption and passed by /ig-human. The Gemini
prompts are the animated, no-speech format Gemini accepted; add the voiceover in your editor from
the table in each reel.

Files:
- `pillar-1-cinematic-prompts.md`, `pillar-2-cinematic-prompts.md`: cinematic prompts (narration, impact text, titles inside each prompt), same format as the refuge area reel. Use these first.
- `pillar-1-why-buy-fire-insurance.md`, `pillar-2-lessons-from-rejected-claims.md`: scripts, facts, sources, captions, plus animated no-speech prompts as a fallback if Gemini refuses a cinematic one.
