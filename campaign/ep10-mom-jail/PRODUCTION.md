# Episode 10 — "Mom Goes to Jail" · Production Package

**Tag line:** *"Glad I learned about that law. I don't want my mom to go to jail!"*

**Rule it teaches:** Parents and guardians can be held responsible for violations committed by minors under their direct control or with their consent or knowledge. Fines stack: $50 → $100 → $500 → $750+.

**Visual style note:** This episode was storyboarded with **gpt-image-2** (OpenAI) rather than the Gemini 3 Pro Image / nano-banana model used in Ep 1. The cinematic painterly look is intentional variety. Match the rest of the series accordingly when you publish.

---

## Total target runtime: ~12 seconds (vertical 9:16)

| Time | Beat | Source |
|---|---|---|
| 0:00–0:06 | Cartoon crash (e-moto into lemonade stand) | Veo 3 generation #1 — image-to-video from `crash-keyframe.png` |
| 0:06 | Hard cut | — |
| 0:06–0:11 | Kid on porch, delivers tag line with synced audio | Veo 3 generation #2 — image-to-video from `recovery-reference.png` |
| 0:11–0:13 | End card | Overlay in editor |

---

## Veo 3 Prompt #1 — The Crash (image-to-video)

**Starting frame:** `campaign/ep10-mom-jail/crash-keyframe.png`
**Tool call (next session):** `generate_video_from_image`
**Duration:** 6 seconds
**Aspect:** 9:16

> The cartoon scene animates forward in playful slow motion. A 12-year-old cartoon kid in a marigold-yellow helmet rides an oversized red dirt-bike-style e-moto and crashes spectacularly through a small wooden suburban lemonade stand. The wooden frame explodes outward into splinters. Yellow lemons fly through the air in graceful slow arcs. Paper cups tumble end-over-end. Yellow lemonade splashes in perfect cinematic curves. Oversized cartoon dollar bills flutter and twirl through the upper portion of the frame in slow motion. A wooden judge's gavel tumbles dramatically end-over-end across the top of the frame, almost falling toward the camera at the very end. The kid's eyes are wide with cartoon surprise, mouth in an 'O,' helmet firmly on. Pixar/Disney 3D cartoon style, bright golden afternoon sunlight, exaggerated slapstick physics, motion blur on the flying objects. The camera holds steady on the chaos, slight subtle handheld jitter. Audio: a wooden splintering crash sound on impact, followed by four rapid cash-register CHA-CHING sounds escalating in pitch ($50… $100… $500… $750!), then a single resonant wooden WHACK as the gavel falls toward camera at the end. No spoken dialogue.

---

## Veo 3 Prompt #2 — The Recovery + Spoken Line (image-to-video)

**Starting frame:** `campaign/ep10-mom-jail/recovery-reference.png`
**Tool call (next session):** `generate_video_from_image`
**Duration:** 5 seconds
**Aspect:** 9:16

> A photorealistic 12-year-old boy with medium-tan skin and short dark hair sits on the porch steps wearing a marigold-yellow bike helmet. He looks directly into the camera with a worried-but-earnest expression — slightly wide eyes, a small concerned mouth, one hand cupped near his cheek in an 'oh no' gesture. He speaks the following line clearly, naturally, with a kid's slightly panicked sincerity, mouth moving in perfect sync with the words: *"Glad I learned about that law. I don't want my mom to go to jail!"* He pauses on the word 'jail,' eyes widening slightly. A smartphone next to him on the step buzzes with an incoming call right as he finishes the line — he glances at it on the last word. Subtle natural body movement throughout. Cinematic warm golden-hour lighting, shallow depth of field, photorealistic documentary aesthetic, slight film grain. Audio: the boy speaks the line in a real preteen voice — slightly worried, earnest, a tiny bit theatrical. Ambient suburban afternoon sounds (distant lawn mower, birds). Phone vibrates against the porch step on the last word.

**Voice direction note:** Veo 3 generates synchronized voice natively. If the first take's voice feels too smooth or too adult, regenerate with the explicit phrase *"voice of a real 12-year-old boy, slightly nervous, mid-pitch, natural inflection"* added to the prompt.

---

## End card (overlay in editor, 0:11–0:13)

```
RULE — Parents can be fined for kids' violations.
                $50  ·  $100  ·  $500  ·  $750+
              → bataviail.gov/e-mobility-guide
```

Match the on-screen typography to the landing page: *Bagel Fat One* for the rule headline, *JetBrains Mono* for the dollar amounts, stop-red highlight on `Parents` and `fined`.

---

## How to fire this in the next session

After you close and reopen Claude Code in this project, just say:

> *"Generate the two Veo 3 clips for the Mom Jail episode using the keyframes in `campaign/ep10-mom-jail/`."*

I'll fire `generate_video_from_image` twice (in parallel) with the two prompts above. Outputs land in `campaign/videos/` as MP4s. Total wall time should be ~3–5 minutes per clip.

---

## Cost note

Veo 3 is billed by Google per second of generated video. Approximate budget for this episode:

- Clip 1 (6s) + Clip 2 (5s) ≈ **11 seconds total** at the standard `veo-3.0-generate-preview` rate
- Quick switch to `veo-3.0-fast-generate-preview` (slightly lower quality, ~40% cheaper) is one env var change in the MCP config if costs come back surprising

Check current pricing in Google AI Studio before running a full batch of 11 episodes.

---

## File index

```
campaign/ep10-mom-jail/
├── crash-keyframe.png       # The chaos frame (gpt-image-2) — Veo clip #1 starting frame
├── recovery-reference.png   # The recovery (gpt-image-2) — Veo clip #2 starting frame
└── PRODUCTION.md            # this file
```

---

## Other tag lines + episode pairings to consider next

Just so you have a roadmap, here's how the rest of your tag-line list maps to episodes from `video-scripts-v2.md`:

| Tag line | Best episode pairing | Rule |
|---|---|---|
| *"Yikes! Glad I wore my helmet!"* | Ep 1 Geese Got Me (already storyboarded with nano-banana) | Helmet under 16 |
| *"Happy I have helmet hair instead of a head injury right now!"* | Alt for Ep 1 — funnier, more sharable | Helmet under 16 |
| *"That could have ruined my whole summer! Happy I wore my helmet."* | Variation for any helmet episode | Helmet under 16 |
| *"Oops, Guess I shouldn't have been on the sidewalk!"* | Ep 2 Sidewalk vs. Warehouse | No e-bikes on sidewalks |
| *"Wow, sidewalks really are for walking not riding."* | Variation on Ep 2 | No e-bikes on sidewalks |
| *"Phew, good thing I stayed in the bike lane."* | Closer to Ep 2 | No e-bikes on sidewalks |
| *"Being honked at was scary, I'll be sure to stay in the bike lane from now on."* | Variation on Ep 2 | No e-bikes on sidewalks |
| *"Wow, good thing I had my night light on so cars could see me."* | Ep 4 Pizza Tower at Midnight | Lights after dark |
| *"Wow, good thing that car could see me at the stop sign this time of night."* | Variation on Ep 4 | Lights after dark |
| *"Almost wiped out there. I should have my hands on the handlebar."* | Ep 3 Marching Band or Ep 7 Fountain | Hands on bars |
| *"That was frightening! Next time, I won't be texting while riding."* | Ep 7 Fountain Selfie | Hands on bars + distracted |
| *"Woah, I could have crashed going over the speed limit like that."* | New episode — Class 3 e-bike at 28 mph | Class 3 speed rules |
| *"Glad I learned about that law. I don't want my mom to go to jail!"* | **THIS EPISODE (Ep 10)** | Parental responsibility |
| *"I need to be careful; I don't want my parents to get in trouble for my reckless riding!"* | Variation on Ep 10 | Parental responsibility |
| *"Woah that was close! Next time I'll remember to obey traffic laws."* | New episode — traffic signal violation | Obey traffic laws |
| *"That could've been bad! I should have used my hand signal when riding."* | New episode — turning without signaling | Hand signals |
| *"Happy I looked both ways before crossing."* | New episode — intersection | Intersections |
| *"Close one! I don't want to hurt others while riding."* | Ep 8 The Yield | Yield to pedestrians |
| *"Maybe flying through crosswalks isn't the move!"* | Variation on Ep 8 | Yield to pedestrians |
| *"Phew, that was close! Guess I better slow down."* | Universal — works with any speed episode | General speed |
| *"Good thing I know what class my e-bike is, so I follow safe riding laws."* | New episode — class label check | Class definitions / labeling |
| *"Yikes, I almost had to learn about safe riding the hard way."* | Universal — could close any episode | General |
