# Retention playbook: keeping viewers to the last second

## Why the current reels lose people

Likely causes, from the reels seen so far:

1. **The first frame is branding, not a reason to stay.** The gold header
   is fine as a frame, but a title card or logo moment at 0:00 is skipped.
2. **Lists, not stories.** "Cause 1, cause 2, prevention 1, 2, 3" gives the
   viewer no reason to wait for the end.
3. **No open loop.** Nothing is promised that only the last second delivers.
4. **AI presenter and AI text.** Viewers sense an AI avatar fast and trust
   it less; garbled AI text makes it worse. Your real face on a phone, in a
   real place, usually holds better. Use AI for b-roll only.
5. **Documentary pace.** Slow narration with long beats. Reels reward short
   lines and a new frame every 2 to 3 seconds.
6. **No money.** Fire safety is abstract; ₹ is not. Every reel should have a
   rupee number or a real place in it.

## 10 retention rules

1. **Start in the middle of the action.** Frame 1 is flames, smoke, a
   burnt room or you pointing at a hazard. Never a title card.
2. **Open a loop in the first 3 seconds and close it in the last 3.**
   "Answer at the end." "The third one is the one nobody checks."
3. **Put a ₹ number or a real place in the first 5 seconds.**
4. **One idea per reel.** If you have three causes, you have three reels.
5. **20 to 35 seconds.** Shorter finishes more often.
6. **Cut every 2 to 3 seconds.** New angle, zoom, b-roll or text card.
7. **Text on screen from frame 1, and captions throughout.** Most people
   start muted.
8. **Speak faster than feels natural.** About 170 to 180 words a minute.
9. **Make them answer.** A guess, a quiz, a "spot the risk": people stay to
   see if they were right, and they comment their answer.
10. **Reveal in the final second, then loop.** The last line echoes the
    first, so the replay feels seamless and counts again.

## 8 formats, with scripts

Hook scores are from `hookscore.py` (wording only; it does not measure the
open loop, which is the real driver for formats 1, 2 and 3).

### 1. Guess the cause (open loop) — hook 60.8

**On screen 0:00:** a burnt bedroom, slow push-in. Card: "Guess the cause 👇"
```
Guess what started this fire.
A. Room heater. B. Phone charger. C. Mosquito coil.
Answer at the end.
Look at the burn marks. Fire burns up and out,
so the deepest, lowest burn points to where it started.
Here. On the mattress. Not near the heater.
Something was lying on the bed, getting hot, with nowhere for the heat to go.
It was the phone charger.
Charge on a hard surface, never under a pillow.
What did you guess? Comment A, B or C.
```
Use a staged or generated scene, not a real customer's photos.

### 2. Spot the risk (game) — film in a real shop, with permission

**On screen 0:00:** you in a shop, phone camera, card: "Spot 3 fire risks ⏱️5"
```
I find fire causes for insurance claims.
This shop has 3 fire risks. Find them before I do.
[5-second timer, still frame]
One. Extension board under the counter, three heaters on it.
Two. Stock touching the tube light.
Three. The extinguisher is behind the boxes. Nobody can reach it.
Got all three? Tell me how many you found.
```
Do not show the shop's name. Rewrite the three risks to what you actually see.

### 3. Would your claim be paid? (quiz with real maths) — hook 60.8

**On screen 0:00:** a burnt shop shutter. Card: "Stock ₹50L · Insured ₹25L · Loss ₹10L"
```
Would your insurance pay for this fire? Most owners get it wrong.
Stock worth 50 lakh. Insured for 25 lakh. The fire destroys 10 lakh.
How much does the insurer pay?
Not 10 lakh.
Under the average condition many fire policies apply,
you were insured for half the value, so you get about half the loss.
5 lakh.
Check your policy wording, and update your sum insured every year.
What did you guess? 10 lakh or 5?
```
⚠ Check the average condition wording on the policies you know before posting.

### 4. Insider: what I check first — hook 74.2

**On screen 0:00:** you walking into a burnt premises (staged), card: "After every fire 🔍"
```
After every fire, I check these 3 things first.
One. Where it started: the lowest, deepest burn.
Two. What was there that shouldn't be: stock next to the panel, a heater by the curtain.
Three. What failed: the extinguisher, the alarm, the locked exit.
Almost every fire I see has all three.
Check them in your home or shop tonight.
Which one would you fail?
```

### 5. "Never do this, watch why" — hook 80.2 (highest)

**On screen 0:00:** a kadhai flaring on a stove. Card: "Never use water 🚫💧"
```
Never pour water on a burning kadhai. Watch why.
Water is heavier than oil, so it sinks to the bottom.
The hot oil turns it to steam in a split second,
and steam takes up about 1,700 times more space.
It throws the burning oil up and out, into a fireball.
Instead: gas off, lid on, leave it covered.
Never water. Gas off, lid on.
```
Use publicly licensed test footage with credit, or a generated clip. Never
film this demonstration yourself.

### 6. POV story (second person, tension)

**On screen 0:00:** dark bedroom, faint smoke under the door. Card: "2:00 a.m."
```
2 a.m. Your house is filling with smoke. You don't wake up.
Smoke doesn't wake sleeping people reliably.
The gases make you drowsier, not more alert.
A smoke alarm outside your bedroom does wake you.
It costs less than a dinner out.
Test it once a month.
It's 2 a.m. Would you wake up?
```

### 7. Countdown (timer on screen)

**On screen 0:00:** a timer starts at 0:00 over a room beginning to burn.
```
Watch the clock.
0:30. A small flame on the sofa. You think you have time.
1:00. Smoke fills the top half of the room.
2:00. You can't see the door.
Modern homes can become deadly in a few minutes.
Know two ways out of every room. Practise them.
How long do you think you'd have?
```
⚠ Use only timings from published fire tests (for example UL research), with
credit, or keep the numbers general as above.

### 8. Cheap cause, expensive loss — hook 50.6 (improve before use)

**On screen 0:00:** close-up of a cracked LPG hose. Card: "₹ hose → ₹ lakh loss"
```
This cheap rubber hose can burn down a restaurant.
Rubber hoses crack with heat and age.
A cracked hose leaks gas next to an open flame.
Check the expiry date printed on the hose.
Change it before that date, not after a leak.
When did you last check yours?
```
Run `/ig-reel` on this one first: the hook needs a stronger stake.

## A 2-week test

Post formats 1, 3, 4, 5 and 2 across two weeks. After 7 days each, note from
Instagram insights: **3-second hold rate, average watch time, completion,
saves, shares, comments**. Run `/ig-audit` with those numbers. Make more of
the two formats that win; drop the rest.
