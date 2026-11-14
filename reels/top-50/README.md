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

## How every script was checked

Every one of the 51 scripts (these 50 plus the refuge area reel) was run
through the Instagram agent skills in this repo, and all 51 pass all three:

- **/ig-reel hook score:** 94 to 100. Each opens with a short question
  ("Can 1 AC cost you everything?") answered by a real number and place.
  "Cost you everything" covers lives and property; no "kill" or "dead".
- **/ig-reel beat sheet:** no line over 4 seconds, a number or name in every
  run of 3 lines, the hook said in under 3 seconds, and the last line loops
  back to a word in the hook so replays feel seamless.
- **/ig-human:** every script PASSES (72 to 80): varied sentence lengths,
  contractions and "you", no AI filler words or hidden characters.

Each Part 3 opens with "Fix 1:", the series' signature line. Numbers are
written as digits ("Can 1 cylinder"); the narrator says them as words.
Each episode file shows its own scores.

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
| 01 | [Hospital ICU Fires](episodes-01-10.md#01-hospital-icu-fires) | Can 1 spark cost your ICU everything? Cuttack lost 10. | 100 |
| 02 | [Hotel Fires](episodes-01-10.md#02-hotel-fires) | Can 1 hotel cost you everything? Delhi lost 21. | 100 |
| 03 | [AC Blast Fires](episodes-01-10.md#03-ac-blast-fires) | Can 1 AC cost you everything? Delhi lost 9. | 100 |
| 04 | [E-Scooter Charging Fires](episodes-01-10.md#04-e-scooter-charging-fires) | Can 1 e-scooter cost you everything? Noida lost 2. | 100 |
| 05 | [Ground-Floor Short Circuits](episodes-01-10.md#05-ground-floor-short-circuits) | Can 1 shop below cost you everything? Hyderabad lost 17. | 100 |
| 06 | [Restaurant Gas Cylinders](episodes-01-10.md#06-restaurant-gas-cylinders) | Can 1 cylinder cost you everything? Never stack 19. | 100 |
| 07 | [Power Bank Fires](episodes-01-10.md#07-power-bank-fires) | Can 1 power bank risk your flight? Never stow it overhead. | 100 |
| 08 | [Pharma Reactor Explosions](episodes-01-10.md#08-pharma-reactor-explosions) | Can 1 reactor cost you everything? Bharuch lost 5. | 100 |
| 09 | [Boiler Explosions](episodes-01-10.md#09-boiler-explosions) | Can 1 boiler cost you everything? Chhattisgarh lost 9. | 100 |
| 10 | [Godown Fire Losses](episodes-01-10.md#10-godown-fire-losses) | Can 1 fire cost you 4.81 crore? Nagpur lost it. | 100 |
| 11 | [Fireworks Factory Blasts](episodes-11-20.md#11-fireworks-factory-blasts) | Can 1 spark cost you everything? Dozens of lives lost. | 100 |
| 12 | [Crackers Stored at Home](episodes-11-20.md#12-crackers-stored-at-home) | Can 1 cracker stock cost you everything? Never keep it home. | 100 |
| 13 | [AC Sleeper Bus Fires](episodes-11-20.md#13-ac-sleeper-bus-fires) | Can 1 bus ride cost you everything? Jaisalmer lost 20. | 100 |
| 14 | [One Exit, No Way Out](episodes-11-20.md#14-one-exit-no-way-out) | Can 1 door cost you everything? Delhi lost 21. | 100 |
| 15 | [Decorative Light Fires](episodes-11-20.md#15-decorative-light-fires) | Can 1 light string cost you your shop? Never leave it on. | 100 |
| 16 | [Showroom Fires](episodes-11-20.md#16-showroom-fires) | Can 1 loose joint cost your showroom? 3 lost in 1 week. | 100 |
| 17 | [Market Fires](episodes-11-20.md#17-market-fires) | Can 1 narrow lane cost you your shop? Jammu lost 40. | 100 |
| 18 | [Chemical Drum Fires](episodes-11-20.md#18-chemical-drum-fires) | Can 1 drum cost you 4 factories? Navi Mumbai lost them. | 100 |
| 19 | [Fires During Repair Work](episodes-11-20.md#19-fires-during-repair-work) | Can 1 repair cost you everything? Chhatral lost 4. | 100 |
| 20 | [High-Rise Fires](episodes-11-20.md#20-high-rise-fires) | Can 1 staircase cost you everything? Nalasopara lost 2. | 100 |
| 21 | [Smoke Strikes First](episodes-21-30.md#21-smoke-strikes-first) | Can 1 breath of smoke cost you everything? Mangolpuri lost workers. | 94 |
| 22 | [Textile and Garment Units](episodes-21-30.md#22-textile-and-garment-units) | Can 1 cylinder cost your factory everything? Surat lost 2. | 100 |
| 23 | [Transformer Fires](episodes-21-30.md#23-transformer-fires) | Can 1 transformer cost you your car? Hafeezpet lost vehicles. | 94 |
| 24 | [CNG Car Fires](episodes-21-30.md#24-cng-car-fires) | Can 1 CNG car fire cost you everything? Barabanki lost 1. | 100 |
| 25 | [Pandal Fires](episodes-21-30.md#25-pandal-fires) | Can 1 spark cost you everything? Goa lost 25. | 100 |
| 26 | [Plastic Factory Fires](episodes-21-30.md#26-plastic-factory-fires) | Can 1 plastic fire cost you your factory? Never stack high. | 100 |
| 27 | [Cold Storage Ammonia](episodes-21-30.md#27-cold-storage-ammonia) | Can 1 cold room cost you everything? Prayagraj lost 4. | 100 |
| 28 | [LPG Tanker Fires](episodes-21-30.md#28-lpg-tanker-fires) | Can 1 tanker cost you everything? Never film it. | 100 |
| 29 | [Cotton Ginning Fires](episodes-21-30.md#29-cotton-ginning-fires) | Can 1 hot silencer cost you? Washim lost 2,000 quintals. | 100 |
| 30 | [Diwali Night Fires](episodes-21-30.md#30-diwali-night-fires) | Can 1 rocket cost you your home? Never store junk. | 100 |
| 31 | [Rooftop Solar Fires](episodes-31-40.md#31-rooftop-solar-fires) | Can 1 solar wire cost your home? Never skip checks. | 100 |
| 32 | [LPG Leaks at Night](episodes-31-40.md#32-lpg-leaks-at-night) | Can 1 switch cost you everything? Never near gas. | 100 |
| 33 | [Short Circuits That Don't Trip](episodes-31-40.md#33-short-circuits-that-dont-trip) | Can 1 short circuit cost you everything? Seoni lost 6. | 100 |
| 34 | [Fire Tender Access](episodes-31-40.md#34-fire-tender-access) | Can 400 metres cost you everything? Goa lost 25. | 100 |
| 35 | [ICU Evacuation Done Right](episodes-31-40.md#35-icu-evacuation-done-right) | Can 1 drill save your patients? Never skip it, not once. | 100 |
| 36 | [Fire NOC and Licences](episodes-31-40.md#36-fire-noc-and-licences) | Can 1 missing NOC cost your claim? Goa lost 25. | 100 |
| 37 | [Illegal Units Near Homes](episodes-31-40.md#37-illegal-units-near-homes) | Can 1 illegal unit cost you everything? Ahmedabad lost 8. | 100 |
| 38 | [Overloaded Wiring](episodes-31-40.md#38-overloaded-wiring) | Can 1 old wire cost you everything? Hyderabad lost 17. | 100 |
| 39 | [Business Interruption](episodes-31-40.md#39-business-interruption) | Can 1 fire cost you 3 months' rent? Not basic policies. | 100 |
| 40 | [Fire Spreads to Neighbours](episodes-31-40.md#40-fire-spreads-to-neighbours) | Can 1 neighbour's fire cost you? 4 factories lost. | 100 |
| 41 | [Vehicles Burned in Fires](episodes-41-50.md#41-vehicles-burned-in-fires) | Can 1 kitchen blast cost you your car? Balasore lost several. | 94 |
| 42 | [Why Fire Cause Matters](episodes-41-50.md#42-why-fire-cause-matters) | Can 1 clean-up cost you your claim? Never clean first. | 100 |
| 43 | [Escape Before You Need It](episodes-41-50.md#43-escape-before-you-need-it) | Can 1 escape plan save you? Never wait, not once. | 100 |
| 44 | [AC Fires in Hotels and Buses](episodes-41-50.md#44-ac-fires-in-hotels-and-buses) | Can 1 hotel AC cost you everything? Kolkata lost 9. | 100 |
| 45 | [Lithium Battery Fires](episodes-41-50.md#45-lithium-battery-fires) | Can 1 swollen battery cost you everything? Never charge it. | 100 |
| 46 | [Stilt Parking Fires](episodes-41-50.md#46-stilt-parking-fires) | Can 1 parking lot cost you everything? Noida lost 2. | 100 |
| 47 | [Restaurant Fires Spread Up](episodes-41-50.md#47-restaurant-fires-spread-up) | Can 1 kitchen fire cost you everything upstairs? Never ignore it. | 94 |
| 48 | [The Underinsurance Trap](episodes-41-50.md#48-the-underinsurance-trap) | Can 1 crore cover only 50 lakh? Never underinsure your stock. | 94 |
| 49 | [Godown Fires at Night](episodes-41-50.md#49-godown-fires-at-night) | Can 1 godown fire cost you crores? Never leave power on. | 100 |
| 50 | [Toxic Gas After Industrial Fires](episodes-41-50.md#50-toxic-gas-after-industrial-fires) | Can 1 blast cost you everything? Bharuch lost 5. | 100 |
