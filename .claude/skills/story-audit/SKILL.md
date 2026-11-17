---
name: story-audit
description: Find the hidden word pattern separating your winning posts from your losing ones. Pulls every reel's real view count, groups hooks by the shape of their opening claim, and reports which shape wins - with the exception count, so you know whether it is a tendency or a rule.
---

# Story audit

You are auditing one account's own back catalogue to find what its winners share and its losers lack.
The output is a short report, not a lecture.

## What makes this work

The account owner has read their own drafts too many times to see the pattern.
You have never read them. That is the entire advantage - so do not reason from marketing theory, reason from their numbers.

## 1. Get the real numbers

Never use a cached file. Views drift, and always upward, so a stale file understates the winners.

- With the Ootto plugin connected in Claude: ask for every reel with its lifetime views.
- Otherwise, Instagram Graph API: page `GET /{ig-user-id}/media` (the default page is ~25 - **you must follow the `after` cursor**, or an account past 25 posts silently truncates), then `GET /{media-id}/insights?metric=views,reach,saved,shares&period=lifetime` per item.

Record: id, timestamp, first line of the caption, views, saves, shares.

## 2. Classify by the SHAPE of the opening claim

Take the **first line only**. That is what decided the scroll.

Sort every hook into one of:

| shape | it says | example |
|---|---|---|
| **ACTION** | what the thing DID, already, in the world | "Claude can now make reels" |
| **INSTRUCTION** | how the reader could USE the thing | "How to turn Claude into a research machine" |
| **neither** | opinion, question, observation | "Your saved notes are a graveyard" |

Classify on grammar, not vibe: a past-tense or already-happened verb attached to the subject is ACTION; an imperative or "how to / here's how / the N ways" frame is INSTRUCTION.

## 3. Report medians, and the exception count

Means lie when one post is a 90th-percentile outlier. Report **median, mean, best, n** per group.

Then the number that actually settles it: **how many losers beat the worst winner.** Zero crossover is a rule; heavy crossover is a tendency. Say which one you found - overclaiming a rule that is only a tendency is the fastest way to lose the reader's trust.

## 4. Write the report

Under 200 words. Structure:

1. **The split** - one sentence, the two shapes and their medians.
2. **The evidence** - three winners with figures, three losers with figures. Real hooks, quoted.
3. **The crossover** - the exception count, stated plainly.
4. **The rewrite** - take their *worst* hook and rewrite it in the winning shape. One line. This is the part they act on.

## 5. Say what you cannot see

Views are shaped by posting time, thumbnail, audio, and luck. You have measured a correlation in one account's history, not a law of the platform. Say so in one sentence and stop - a caveat paragraph undoes the finding.

## Worked result

Run on @jayantcreates.ai, 72 reels, live pull 2026-08-11:

- ACTION: n=29, median 1,933, best **97,860**
- INSTRUCTION: n=6, median 1,238, best **1,696**
- Crossover: none. No instruction hook has ever cleared 1,700 views on the account.

Winners: "Claude can now make reels" 97,860 · "I let Claude run my Instagram for 6 days" 20,909 · "Claude hacked my Instagram" 6,859
Losers: "This is how to turn Claude into a social media savant" 1,696 · "How to turn Claude into a content research machine" 1,082 · "This is how to use Claude to write hooks" 485

Rewrite of the worst: "This is how to use Claude to write hooks" → "Claude wrote the hook that did 97,860 views."
