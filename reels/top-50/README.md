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

Every reel opens with a short, surprising question in the first 3 seconds,
answered at once by a real number ("Can your AC kill you? Nine killed in
Delhi."). Scored with `hookscore.py`: 48 of 50 score 94 or 100; episodes 35
and 50 score 88 and 84 because the higher-scoring wording would have
misstated the facts. Numbers right after "Can" are written as digits ("Can 1
cylinder…"): the narrator still says "one", and captions read faster. Spoken lengths were timed at 165 words a
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
| 01 | [Hospital ICU Fires](episodes-01-10.md#01-hospital-icu-fires) | Can your ICU kill you? One short circuit killed ten patients. | 94 |
| 02 | [Hotel Fires](episodes-01-10.md#02-hotel-fires) | Can your hotel kill you? Twenty-one killed in Delhi. | 100 |
| 03 | [AC Blast Fires](episodes-01-10.md#03-ac-blast-fires) | Can your AC kill you? Nine killed in Delhi. | 100 |
| 04 | [E-Scooter Charging Fires](episodes-01-10.md#04-e-scooter-charging-fires) | Can your e-scooter kill you? Two killed in Noida. | 100 |
| 05 | [Ground-Floor Short Circuits](episodes-01-10.md#05-ground-floor-short-circuits) | Can a shop kill you upstairs? Seventeen killed in Hyderabad. | 100 |
| 06 | [Restaurant Gas Cylinders](episodes-01-10.md#06-restaurant-gas-cylinders) | Can 1 cylinder kill you? Never stack them. Delhi saw 3 explode. | 94 |
| 07 | [Power Bank Fires](episodes-01-10.md#07-power-bank-fires) | Can 1 power bank kill you? Never stow it overhead. | 100 |
| 08 | [Pharma Reactor Explosions](episodes-01-10.md#08-pharma-reactor-explosions) | Can one reactor kill you? Five workers killed in Bharuch. | 100 |
| 09 | [Boiler Explosions](episodes-01-10.md#09-boiler-explosions) | Can your boiler kill you? Nine workers killed in April. | 100 |
| 10 | [Godown Fire Losses](episodes-01-10.md#10-godown-fire-losses) | Can one fire cost you 4.81 crore? Nagpur lost it overnight. | 100 |
| 11 | [Fireworks Factory Blasts](episodes-11-20.md#11-fireworks-factory-blasts) | Can one spark kill you? Three fireworks blasts killed dozens. | 94 |
| 12 | [Crackers Stored at Home](episodes-11-20.md#12-crackers-stored-at-home) | Can crackers kill you at home? Never store them. Siwan shows why. | 94 |
| 13 | [AC Sleeper Bus Fires](episodes-11-20.md#13-ac-sleeper-bus-fires) | Can your bus kill you? Twenty killed on one sleeper bus. | 100 |
| 14 | [One Exit, No Way Out](episodes-11-20.md#14-one-exit-no-way-out) | Can one door kill you? Twenty-one killed in Delhi. | 100 |
| 15 | [Decorative Light Fires](episodes-11-20.md#15-decorative-light-fires) | Can 1 light string kill you? Never leave it on overnight. | 100 |
| 16 | [Showroom Fires](episodes-11-20.md#16-showroom-fires) | Can 1 loose joint kill you? Three showrooms lost in one week. | 94 |
| 17 | [Market Fires](episodes-11-20.md#17-market-fires) | Can 1 narrow lane cost you? Jammu lost 40 shops. | 100 |
| 18 | [Chemical Drum Fires](episodes-11-20.md#18-chemical-drum-fires) | Can one drum cost you four factories? Navi Mumbai lost them. | 100 |
| 19 | [Fires During Repair Work](episodes-11-20.md#19-fires-during-repair-work) | Can repairs kill you? Four killed in Chhatral. | 100 |
| 20 | [High-Rise Fires](episodes-11-20.md#20-high-rise-fires) | Can your stairs kill you? Two killed in Nalasopara. | 100 |
| 21 | [Smoke Kills First](episodes-21-30.md#21-smoke-kills-first) | Can smoke kill you first? Workers died of smoke in Mangolpuri. | 94 |
| 22 | [Textile and Garment Units](episodes-21-30.md#22-textile-and-garment-units) | Can one cylinder kill you at work? Surat lost two workers. | 100 |
| 23 | [Transformer Fires](episodes-21-30.md#23-transformer-fires) | Can a transformer kill you? Hafeezpet lost vehicles in March. | 94 |
| 24 | [CNG Car Fires](episodes-21-30.md#24-cng-car-fires) | Can 1 CNG car fire kill you? A Barabanki driver was killed. | 100 |
| 25 | [Pandal Fires](episodes-21-30.md#25-pandal-fires) | Can one spark kill you? Twenty-five killed in Goa. | 100 |
| 26 | [Plastic Factory Fires](episodes-21-30.md#26-plastic-factory-fires) | Can 1 plastic fire kill you? Never stack high. | 100 |
| 27 | [Cold Storage Ammonia](episodes-21-30.md#27-cold-storage-ammonia) | Can 1 cold room kill you? Four killed in Prayagraj. | 100 |
| 28 | [LPG Tanker Fires](episodes-21-30.md#28-lpg-tanker-fires) | Can a tanker kill you? Never film it. Kaushambi lost four. | 100 |
| 29 | [Cotton Ginning Fires](episodes-21-30.md#29-cotton-ginning-fires) | Can 1 hot silencer cost you? 2,000 quintals lost in Washim. | 100 |
| 30 | [Diwali Night Fires](episodes-21-30.md#30-diwali-night-fires) | Can 1 rocket cost you your home? Never store junk on balconies. | 94 |
| 31 | [Rooftop Solar Fires](episodes-31-40.md#31-rooftop-solar-fires) | Can 1 bad solar wire cost you your home? Never skip checks. | 100 |
| 32 | [LPG Leaks at Night](episodes-31-40.md#32-lpg-leaks-at-night) | Can 1 switch kill you? Never touch it if you smell gas. | 100 |
| 33 | [Short Circuits That Don't Trip](episodes-31-40.md#33-short-circuits-that-dont-trip) | Can 1 short circuit kill you? Six killed in Seoni. | 100 |
| 34 | [Fire Tender Access](episodes-31-40.md#34-fire-tender-access) | Can 400 metres kill you? Goa's fire tankers waited there. Twenty-five killed. | 94 |
| 35 | [ICU Evacuation Done Right](episodes-31-40.md#35-icu-evacuation-done-right) | Can 1 drill save your patients? Never skip it. Ten killed in Cuttack. | 88 |
| 36 | [Fire NOC and Licences](episodes-31-40.md#36-fire-noc-and-licences) | Can no NOC kill your claim? Twenty-five died in one Goa club. | 94 |
| 37 | [Illegal Units Near Homes](episodes-31-40.md#37-illegal-units-near-homes) | Can 1 illegal unit kill you? Eight killed in Ahmedabad. | 100 |
| 38 | [Overloaded Wiring](episodes-31-40.md#38-overloaded-wiring) | Can your wiring kill you? Seventeen killed in Hyderabad. | 100 |
| 39 | [Business Interruption](episodes-31-40.md#39-business-interruption) | Can 1 fire cost you 3 months' rent? Not on a basic policy. | 94 |
| 40 | [Fire Spreads to Neighbours](episodes-31-40.md#40-fire-spreads-to-neighbours) | Can 1 neighbour's fire cost you? Four factories lost to one. | 100 |
| 41 | [Vehicles Burned in Fires](episodes-41-50.md#41-vehicles-burned-in-fires) | Can 1 kitchen blast cost you your car? Balasore lost several. | 94 |
| 42 | [Why Fire Cause Matters](episodes-41-50.md#42-why-fire-cause-matters) | Can no cause kill your claim? Never clean up. Seoni called forensics. | 94 |
| 43 | [Escape Before You Need It](episodes-41-50.md#43-escape-before-you-need-it) | Can you escape without a plan? Never. Lucknow students jumped. | 94 |
| 44 | [AC Fires in Hotels and Buses](episodes-41-50.md#44-ac-fires-in-hotels-and-buses) | Can 1 hotel AC kill you? Nine killed in Kolkata. | 100 |
| 45 | [Lithium Battery Fires](episodes-41-50.md#45-lithium-battery-fires) | Can 1 swollen battery kill you? Never charge it. | 100 |
| 46 | [Stilt Parking Fires](episodes-41-50.md#46-stilt-parking-fires) | Can your parking kill you? Two killed in Noida. Never charge there. | 94 |
| 47 | [Restaurant Fires Spread Up](episodes-41-50.md#47-restaurant-fires-spread-up) | Can 1 kitchen fire kill you upstairs? Never ignore it. | 100 |
| 48 | [The Underinsurance Trap](episodes-41-50.md#48-the-underinsurance-trap) | Can 1 crore cover only 50 lakh? Never underinsure your stock. | 94 |
| 49 | [Godown Fires at Night](episodes-41-50.md#49-godown-fires-at-night) | Can 1 godown fire cost you crores? Never leave power on. | 100 |
| 50 | [Toxic Gas After Industrial Fires](episodes-41-50.md#50-toxic-gas-after-industrial-fires) | Can 1 blast leak toxic gas on you? Five killed in Bharuch. | 84 |
