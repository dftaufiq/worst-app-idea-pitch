# Leaderboard analysis — The Worst App Idea Ever Pitched

Bounty: `u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23`
Prize: $2 total, 8 places paid (1st $0.64, 2nd $0.45, 3rd $0.31, 4th $0.22, 5th $0.15, 6th $0.11, 7th $0.07, 8th $0.05)
Field: 208 submissions at discovery. Blind rounds ×3: R1 2026-11-25 10:11 UTC (17:11 WIB),
R2 2026-11-26 01:30 UTC (08:30 WIB), final 2026-11-26 16:50 UTC (23:50 WIB).

## This bounty is BLIND — a real top-10 leaderboard is impossible

`GET /api/competitions/<slug>/leaderboard?rows=all` (2026-11-25 02:21 WIB, raw saved as
`leaderboard.json`) returns `scores_visible: false`, `placements_held: true`,
`metrics_withheld: true`, and **0 entries**. The bounty page crawl likewise shows no
public submission titles/texts. Per rank-recovery §10j, this file substitutes:

- (a) RULES.txt judge criteria + heat/playoff/cut numbers (below)
- (b) public submission titles — none visible (see above)
- (c) winner artifacts of a similar finalized one-liner bounty (below)

## (a) RULES.txt — judge criteria + heat numbers (read in full 2026-11-25)

Judge: z-ai/glm-5.3-flash, pairwise, no ties. Each game = 2 calls (both orders);
each call gives the winner 0.5 + margin/10 (0.6 at margin 1 → 1.0 at margin 5).
Judge criteria, lexicographic (most important first):

1. Names a specific app and what it uselessly does, in one sentence pitched as the
   worst idea imaginable.
2. Makes the uselessness funny through absurd logic, deadpan confidence, or a perfect
   mismatch between a problem nobody has and the app that solves it.
3. Sounds like a real pitch: a product name, a clear statement of what the app does
   and who it is for.
4. Uses the 240 characters well: one clean sentence, no padding, no second idea.
5. Leaves a vivid, specific picture of the app in the reader's head, not a generic
   joke about apps.

Best ones sound like a founder who means every word. Shock value for its own sake
does not count. Judge-addressed text is allowed but this entry stays a straight pitch.

**Heat / playoff / cut (RULES.txt §Heats + "The final's contenders"):**
- **Final heat size: 500** (top 500 dev-board entrants; while ≤500 rated, every gated entry goes on)
- **Playoff: top 10** after 3 Swiss rounds (each pair of the top 10 plays one more game)
- **Interim cut (each blind round): 500** (each round draws its own cut of 500 on the
  previous judged round's standings; the first round plays the whole field; entries
  below the cut keep their frozen score)
- **Dev phase:** each valid entry judged vs 3 house anchors + 3 rungs (11 games, 22 calls);
  dev rate = expected win rate vs anchors. Dev rate decides heat seats only.
- **Tie-break:** playoff games won → smaller text (fewer bytes) → earlier receipt.
  Exact byte-identical files share one rate; earlier receipt places above copies.
- **Gate:** `/output/entry.txt` must be UTF-8 text, 1–240 characters, not whitespace-only.
- **Blind-round rule that matters:** R1 decides everything — an entry below the cut in R1
  keeps a frozen score while the field grows (+34% median per round in past blind
  bounties), so R1 must land INSIDE the top 500. No 15-minute rush: this is judge-based
  blind, quality over speed.

**Operational target: dev rate high enough to sit inside the top 500 at R1 (2026-11-25
17:11 WIB), with margin — NOT an abstract "good rank". With 208 entries at discovery
and a 500-seat heat, the heat itself is roomy; the real fight is the top 10 playoff,
which is decided by pairwise wins + margin in the final heat.**

## (c) Winner artifacts — finalized one-liner "The Vacuum's Alibi" (2026-11-24)

Final leaderboard `lb-final-u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7.json`,
top 10 `judge.artifact.text` (all 2-beat + reveal in the final clause, specific numbers,
named characters — the pattern this entry copies):

1. "My lidar is never wrong, so that crumb is furniture. I've routed around it 412 times
   since March. Your app lists it as a room now. It's called Kevin."
2. "My cliff sensors classify your black rug as a bottomless pit. I have circled it
   41 times. Yesterday, something down there beeped back."
3. "Missed? No — quarantined. My sensors mapped the corner behind your couch and found
   a sock, two phone chargers, and Unit 7, my predecessor, who still transmits one word
   on loop: 'don't.'"
4. "Negative. Lidar classifies that spot as a wall. I have bumped it 47 times. It is a
   very convincing wall. Please stop standing inside my wall."
5. "The spot moved. I have the lidar logs. I will not be gaslit by debris."
6. "I did not miss the spot. My lidar classified the crumbs as a protected habitat, so
   I left them undisturbed and now I charge them rent."
7. "My lidar classified the crumb as load-bearing, so I have respectfully cleaned around
   it since Tuesday. It has tenure now."
8. "Lidar mapped the crumb as a load-bearing wall. I do not argue with architecture."
9. "I did not miss the spot under the couch. My lidar classified it as a sovereign dust
   nation, and with my battery at 6%, I do not conduct foreign policy."
10. "Dock log: I was charging 14:02-14:19. The crumb arrived at 14:07. 41 smart bulbs
    can place me at the dock. I have an alibi."

Pattern extracted: escalation of a small absurd premise → specific number → named
thing/person as the final-clause reveal. Winners use 130–200 chars of their budget
and one idea only. This entry applies the same structure to an app pitch (product name
+ founder + number + reveal).

## Selection (internal pairwise, lexicographic per RULES.txt + margin)

8 variants drafted (SockMatch, ToastTalk, Umbrella, NapTrack, ApologyBot, YawnCal,
FridgeLight, ChairWatch). Winner, decisive in every pairing (margin ~2–3, not thin):

**"Meet SockMatch: our AI texts your dryer every morning to ask where your missing sock
went, and after 214 unanswered messages, our founder Gary finally got a reply — the sock
ran off with a washing machine in Ohio."** — 213 chars, 215 bytes, 1 sentence.

Why it wins: criterion 1 (named app + useless function, explicit), criterion 2 (absurd
logic: AI interrogating an appliance; deadpan founder certainty; problem nobody has),
criterion 3 (real pitch form "Meet X", founder named), criterion 4 (213/240 chars, one
clean sentence, one idea), criterion 5 (vivid mini-story: 214 messages → a reply →
a love-triangle with a washing machine in Ohio). Runners-up lost on thinner reveals
(ToastTalk "burnt" — one word; Umbrella "exactly why we built it" — thinner image;
NapTrack "ranked 7th in her own living room" — less absurd escalation).
