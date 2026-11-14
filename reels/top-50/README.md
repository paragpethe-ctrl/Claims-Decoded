# Fire Claims Decoded: 50 reels, 150 Gemini prompts

Each reel is about 30 seconds: three clips of 10 seconds, one Gemini prompt
per clip. Every prompt carries the same on-screen titles, style, captions, Indian
English voiceover and (in part 3) the end card, word for word. No frame and
no presenter: full-screen b-roll throughout. Only the subtitle changes: it
is the topic of that episode.

Title colours: "FIRE CLAIMS DECODED" in amber-gold (#FFB300) with a soft
shadow; the topic subtitle in white (#FFFFFF) on a 60% black strip with a
red-orange (#FF4D00) accent line. Impact words red and yellow; captions
white with the spoken word in yellow. Warm gold and white read clearly over
fire footage; red is kept for impact words so it never fights the title.

## How each reel is built

| part | seconds | what happens | presenter |
|---|---|---|---|
| 1 | 0 to 10 | Hook spoken on the first frame with a bass hit, then 2 or 3 real incidents | no |
| 2 | 10 to 20 | The engineer's "why it happens" | no |
| 3 | 20 to 30 | Fixes, then the closing question over a single flame in darkness (the series' signature shot), then the end card | no |

End card on every reel: FIRE CLAIMS DECODED · @parag_pethe1 · FOLLOW · 1 FIRE CAUSE EVERY REEL

Hooks were scored with the `hookscore.py` tool in this repo: all 50 score
62 or above, most between 80 and 94. Spoken lengths were timed at 165 words a
minute; every part fits its clip.

## Before you generate

1. **No photo upload needed.** Every clip is b-roll with voiceover.
2. **Check every word Gemini draws.** The prompts ask for the titles,
   impact words, captions and end card. AI video often misspells text. If it
   does, generate without those lines and add the titles, captions (CapCut
   auto captions) and end card in your editor instead.
3. **Re-check the incident facts on the day you post.** Each episode lists
   what was reported and the sources. Death tolls and causes are often
   revised. Where reports conflict, the script avoids the number.
4. **No victims' names, no real footage you don't have rights to.** All
   visuals are generated b-roll.
5. **Episodes 10, 36, 39, 42 and 48 make insurance points.** They say "can"
   and "check your policy wording" on purpose. Adjust them to the policy
   wordings you know.
6. **Episode 31 (solar) comes from a single incident register.** Confirm
   both incidents in local news before posting.

## The 50 episodes

| # | topic | hook | score |
|---|---|---|---|
| 01 | [Hospital ICU Fires](episodes-01-10.md#01-hospital-icu-fires) | One short circuit killed ten ICU patients. Your hospital could be next. | 83 |
| 02 | [Hotel Fires](episodes-01-10.md#02-hotel-fires) | Twenty-one killed in one Delhi hotel. Would you get out of yours? | 83 |
| 03 | [AC Blast Fires](episodes-01-10.md#03-ac-blast-fires) | Never ignore a noisy AC. Nine killed after an AC blast in Delhi. | 87 |
| 04 | [E-Scooter Charging Fires](episodes-01-10.md#04-e-scooter-charging-fires) | Never charge your e-scooter in the parking. Two people died in Noida. | 83 |
| 05 | [Ground-Floor Short Circuits](episodes-01-10.md#05-ground-floor-short-circuits) | Never sleep above a shop without a smoke alarm. Seventeen killed in Hyderabad. | 87 |
| 06 | [Restaurant Gas Cylinders](episodes-01-10.md#06-restaurant-gas-cylinders) | Never stack cylinders in your kitchen. Three exploded in one Delhi fire. | 83 |
| 07 | [Power Bank Fires](episodes-01-10.md#07-power-bank-fires) | Never put your power bank in the overhead bin. One caught fire on IndiGo. | 76 |
| 08 | [Pharma Reactor Explosions](episodes-01-10.md#08-pharma-reactor-explosions) | Five workers killed when a reactor exploded. Your plant runs the same risk. | 88 |
| 09 | [Boiler Explosions](episodes-01-10.md#09-boiler-explosions) | Nine killed in one boiler blast. Is your boiler inspected? | 81 |
| 10 | [Godown Fire Losses](episodes-01-10.md#10-godown-fire-losses) | You lost 4.81 crore in one night. Could you prove it to your insurer? | 69 |
| 11 | [Fireworks Factory Blasts](episodes-11-20.md#11-fireworks-factory-blasts) | Three fireworks blasts. Dozens killed. Is your lane next? | 84 |
| 12 | [Crackers Stored at Home](episodes-11-20.md#12-crackers-stored-at-home) | Never store Diwali crackers at home. Siwan shows why. | 83 |
| 13 | [AC Sleeper Bus Fires](episodes-11-20.md#13-ac-sleeper-bus-fires) | Twenty killed on one sleeper bus. Would you find your exit? | 84 |
| 14 | [One Exit, No Way Out](episodes-11-20.md#14-one-exit-no-way-out) | One door. No way out. Twenty-one killed. Would you find another exit? | 94 |
| 15 | [Decorative Light Fires](episodes-11-20.md#15-decorative-light-fires) | Never leave festive lights on all night. One mall caught fire this month. | 77 |
| 16 | [Showroom Fires](episodes-11-20.md#16-showroom-fires) | Never ignore a warm switch in your showroom. Three burned in one week. | 82 |
| 17 | [Market Fires](episodes-11-20.md#17-market-fires) | Forty shops lost in one night. Can a fire tender reach your shop? | 82 |
| 18 | [Chemical Drum Fires](episodes-11-20.md#18-chemical-drum-fires) | Never store chemical drums together. One fire spread to four factories. | 82 |
| 19 | [Fires During Repair Work](episodes-11-20.md#19-fires-during-repair-work) | Your plant is riskiest during repairs. Four killed in Chhatral. | 64 |
| 20 | [High-Rise Fires](episodes-11-20.md#20-high-rise-fires) | Never store anything in your stairwell. Two died in a Nalasopara high-rise. | 83 |
| 21 | [Smoke Kills First](episodes-21-30.md#21-smoke-kills-first) | Smoke kills you before the flames do. Workers died of smoke in Mangolpuri. | 88 |
| 22 | [Textile and Garment Units](episodes-21-30.md#22-textile-and-garment-units) | Never keep cooking cylinders in your factory. Surat lost two workers. | 94 |
| 23 | [Transformer Fires](episodes-21-30.md#23-transformer-fires) | Never park under a transformer. Hafeezpet lost vehicles in March. | 93 |
| 24 | [CNG Car Fires](episodes-21-30.md#24-cng-car-fires) | Never ignore a gas smell in your CNG car. A driver died in Barabanki. | 76 |
| 25 | [Pandal Fires](episodes-21-30.md#25-pandal-fires) | One spark killed twenty-five in Goa. Your pandal has the same fuel. | 83 |
| 26 | [Plastic Factory Fires](episodes-21-30.md#26-plastic-factory-fires) | Your sprinklers can't stop plastic. Ghaziabad lost a factory this month. | 80 |
| 27 | [Cold Storage Ammonia](episodes-21-30.md#27-cold-storage-ammonia) | Four killed in a cold storage collapse. Your cold room hides the same risk. | 82 |
| 28 | [LPG Tanker Fires](episodes-21-30.md#28-lpg-tanker-fires) | Never stop to film a burning tanker. Kaushambi shows why. | 86 |
| 29 | [Cotton Ginning Fires](episodes-21-30.md#29-cotton-ginning-fires) | One hot silencer lost 2,000 quintals of cotton. Is your yard next? | 80 |
| 30 | [Diwali Night Fires](episodes-21-30.md#30-diwali-night-fires) | 257 fire calls in one Delhi night. Never leave junk on your balcony. | 82 |
| 31 | [Rooftop Solar Fires](episodes-31-40.md#31-rooftop-solar-fires) | Never skip your solar inspection. An Etawah house caught fire two months after installation. | 79 |
| 32 | [LPG Leaks at Night](episodes-31-40.md#32-lpg-leaks-at-night) | Never switch on a light if you smell gas. Three died in Miryalguda. | 82 |
| 33 | [Short Circuits That Don't Trip](episodes-31-40.md#33-short-circuits-that-dont-trip) | Your MCB won't stop this fire. Six died in Seoni. | 84 |
| 34 | [Fire Tender Access](episodes-31-40.md#34-fire-tender-access) | Twenty-five killed while fire tankers waited 400 metres away. Could they reach you? | 82 |
| 35 | [ICU Evacuation Done Right](episodes-31-40.md#35-icu-evacuation-done-right) | Ten killed in one ICU fire. A day later, nobody died in another. Why? | 62 |
| 36 | [Fire NOC and Licences](episodes-31-40.md#36-fire-noc-and-licences) | No fire NOC? Your claim can get complicated. Twenty-five died in one Goa club. | 79 |
| 37 | [Illegal Units Near Homes](episodes-31-40.md#37-illegal-units-near-homes) | Your neighbour's illegal unit is your risk too. Eight killed in Ahmedabad. | 83 |
| 38 | [Overloaded Wiring](episodes-31-40.md#38-overloaded-wiring) | Never add an AC without a load check. Seventeen killed in Hyderabad. | 93 |
| 39 | [Business Interruption](episodes-31-40.md#39-business-interruption) | Never rely on a basic fire policy for rent. Forty Jammu shops shut in one night. | 66 |
| 40 | [Fire Spreads to Neighbours](episodes-31-40.md#40-fire-spreads-to-neighbours) | One fire, four factories lost. Your neighbour's fire is your risk. | 94 |
| 41 | [Vehicles Burned in Fires](episodes-41-50.md#41-vehicles-burned-in-fires) | Never park beside a restaurant kitchen. Balasore lost cars in one blast. | 84 |
| 42 | [Why Fire Cause Matters](episodes-41-50.md#42-why-fire-cause-matters) | No cause, no settlement. Your claim waits for the fire investigation. | 80 |
| 43 | [Escape Before You Need It](episodes-41-50.md#43-escape-before-you-need-it) | Students jumped to escape a fire. Never wait to make your escape plan. | 75 |
| 44 | [AC Fires in Hotels and Buses](episodes-41-50.md#44-ac-fires-in-hotels-and-buses) | Never ignore a burning smell in your hotel room. Nine killed in Kolkata. | 88 |
| 45 | [Lithium Battery Fires](episodes-41-50.md#45-lithium-battery-fires) | Never charge a swollen battery. One chemistry caused three fires this year. | 82 |
| 46 | [Stilt Parking Fires](episodes-41-50.md#46-stilt-parking-fires) | Never charge in stilt parking. Your family lives right above it. | 80 |
| 47 | [Restaurant Fires Spread Up](episodes-41-50.md#47-restaurant-fires-spread-up) | Never sit above a dirty kitchen duct. A Delhi restaurant fire climbed four floors. | 78 |
| 48 | [The Underinsurance Trap](episodes-41-50.md#48-the-underinsurance-trap) | Insured for 1 crore, lost 1 crore, paid 50 lakh. Don't let this be you. | 77 |
| 49 | [Godown Fires at Night](episodes-41-50.md#49-godown-fires-at-night) | Never leave your godown without switching off the main. Three lost crores. | 94 |
| 50 | [Toxic Gas After Industrial Fires](episodes-41-50.md#50-toxic-gas-after-industrial-fires) | The fire is out, but the gas can still kill you. Five killed in Bharuch. | 73 |
