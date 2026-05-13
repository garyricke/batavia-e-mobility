# Photoreal Crash Library — Middle School Edition

A shared library of 6 photorealistic, comedic crash keyframes featuring **AI-generated middle school riders (≈11–14)**. Pairs with real-Batavia-kid recovery footage to form complete two-shot videos.

**The structural rule that makes this work:** the AI clip ENDS at the moment of imminent impact — never showing actual contact, never showing injury. The live footage of the real Batavia kid takes over for the post-impact "phew, I'm fine, glad I learned" recovery. Audience imagination fills the gap between the two cuts; that's where the comedy lands.

Cast on every clip wears a helmet (with a small yellow star sticker — campaign continuity with the landing-page illustrations). Even when they're crashing, the helmet is on. Reinforces the campaign's primary rule even subliminally.

---

## Library contents

| # | File | Rider | Helmet | Scenario | Pair with tag line |
|---|---|---|---|---|---|
| 01 | `01-phone-fail.png` | 12yo Latino boy | navy | E-scooter, phone in hand, mid-stumble on sidewalk. Backpack on. | *"That was frightening! Next time, I won't be texting while riding."* |
| 02 | `02-hedge-slam.png` | 13yo Black girl | hot pink | E-bike, just clipped a hedge on a sidewalk. Leaves exploding. | *"Oops, guess I shouldn't have been on the sidewalk!"* |
| 03 | `03-car-door.png` | 13yo Asian boy | sky blue | E-bike, mid-flight over an open car door downtown. Bag contents airborne. | *"Phew, that was close! Guess I better slow down."* |
| 04 | `04-crosswalk-fail.png` | 12yo white girl | marigold | E-scooter, mid-skid through a crosswalk, yellow sedan braking hard. | *"Happy I looked both ways before crossing."* |
| 05 | `05-no-lights.png` | 13yo Black boy | purple | Unlit e-bike at twilight, mid-swerve in car headlights. Bike lamp visibly OFF. | *"Wow, good thing that car could see me at the stop sign this time of night."* |
| 06 | `06-wheelie-wipeout.png` | 14yo white boy | red | Red e-moto wheelie gone too vertical, falling backward. | *"I need to be careful; I don't want my parents to get in trouble for my reckless riding!"* |

Adult versions of these scenarios are archived in `_archive-adults/` if ever needed.

---

## Recommended model: Sora 2 (with Kling 2.5 Turbo Pro fallback)

**Primary:** `fal-ai/sora-2/image-to-video` — best photoreal kid motion + native audio.

**Fallback:** `fal-ai/kling-video/v2.5-turbo/pro/image-to-video` — silent, layer SFX in editor. Use this if Sora 2's content moderation flags any of the photoreal-minors-in-near-disaster prompts. (Real possibility — OpenAI's policy on minors in distress can be conservative even for comedic safety-education content. If a clip refuses, immediately re-run on Kling with `cfg_scale: 0.5` and we move on. Kling has been more permissive in practice.)

**Sora 2 parameters** (from `fal-video-model-quirks`):
- `duration: 4` (integer; shortest available, perfect for impact-buildup)
- `aspect_ratio: "9:16"` (must be explicit; default is auto)
- `resolution: "720p"` → 720×1280 @ 30fps
- queue-based — `submit_job` + poll, not `run_model`

**Kling 2.5 fallback parameters:**
- `duration: "5"` (string, enum 5 or 10; 5 is fine)
- Aspect inherits from keyframe (already 9:16 for nano-banana shots; openai-images shots are 1024×1536 ≈ 2:3 — close enough, will be padded or trimmed slightly)
- silent output

---

## Per-clip Sora 2 prompts (the cut-at-impact pattern)

Every motion prompt below is structured the same way:
1. The action progresses naturally from the keyframe state for ~3 seconds
2. The clip's last frame is the moment *immediately before* contact
3. Audio cuts hard at that same moment — silence is part of the cut
4. **Never** describe the impact happening, the kid hitting anything, blood, injury, crying, or post-fall state — that's the live footage's job

### Clip 01 — Phone Fail (Sora 2, 4s)

**Starting frame:** `campaign/crash-library/01-phone-fail.png`

> The 12-year-old boy in the navy helmet continues his stumble forward off the electric scooter. His airborne phone completes one slow rotation through the air, still falling toward the sidewalk. His knees bend further, his free arm windmills harder. The scooter rolls slowly forward beneath him without him on it. His mouth stays wide open in cartoon-O surprise. In the final fraction of a second, both his feet are about to leave the deck entirely and his hands are reaching out for the sidewalk. Freeze the clip at the moment immediately before his palms make contact with the concrete — the audience never sees the catch. Bright midday suburban sunlight, slight handheld camera tremor, photorealistic candid iPhone aesthetic. Audio: scooter rolling on concrete, the boy's high-pitched preteen 'WOAHHHH' rising in pitch, then cutting to silence on the freeze. NO impact sound, NO falling sound, NO injury sound.

### Clip 02 — Hedge Slam (Sora 2, 4s)

**Starting frame:** `campaign/crash-library/02-hedge-slam.png`

> The 13-year-old girl in the hot-pink helmet continues her sideways tumble toward the leafy hedge. Green leaves erupt outward in a slow expanding cloud around her. The sky-blue electric bicycle continues falling beneath her. Her outstretched arm reaches further into the hedge, her smile shifts from surprise toward incredulous mid-laugh. In the final fraction of a second, her shoulder and side are about to disappear fully into the foliage — but the camera freezes just before they do. Bright midday sunlight, vivid color, slight motion blur, photorealistic candid iPhone footage. Audio: bike tire scraping on sidewalk, dry rustle of leaves, the girl's preteen 'AHHH—' starting to turn into a laugh, the bark of a neighborhood dog, then sudden silence on the freeze. NO contact thud, NO actual crash sound.

### Clip 03 — Car Door (Sora 2, 4s)

**Starting frame:** `campaign/crash-library/03-car-door.png`

> The 13-year-old boy in the sky-blue helmet continues his slow-motion arc over the top of the open car door. The metal water bottle, notebook, and stuffed-animal keychain rotate through the air on different trajectories. His backpack strap is flapping. The bike completes its drop to the asphalt beneath him. His helmet stays firmly on his head. His expression shifts from initial cartoon-O surprise toward a 'this is happening' wide-eyed acceptance. In the final fraction of a second, his hand is about to touch down on the far side of the door. Freeze immediately before contact. Late-afternoon golden-hour light, brick downtown backdrop, slight motion blur. Photorealistic candid iPhone footage. Audio: initial THWACK of body grazing the door, bike clattering to the street, multiple object-bounces airborne, the boy's drawn-out preteen 'OHHH NOOO,' then a hard cut to silence. NO landing thud.

### Clip 04 — Crosswalk Fail (Sora 2, 4s)

**Starting frame:** `campaign/crash-library/04-crosswalk-fail.png`

> The 12-year-old girl in the marigold helmet continues her sideways skid across the crosswalk. The yellow sedan's grille looms slightly closer but is clearly slowing rapidly. The driver's eyes are visibly wide through the windshield. The girl's scooter wheels squeal across the white crosswalk paint. Her reaching hand stretches further toward the bars. Her ponytail whips with the motion. In the final fraction of a second, the sedan is fully stopped and there is exactly a foot of clearance between her scooter and the car's grille — frozen at the precise moment of maximum tension. NO contact. Bright daytime, downtown brick storefronts, slight motion blur on wheels and grille. Photorealistic candid iPhone capture. Audio: tire screech, the long aggressive sustained CAR HORN, the girl's piercing preteen 'AHHHH,' cuts to silence on the freeze. NO impact sound (because there is no impact).

### Clip 05 — No Lights (Sora 2, 4s)

**Starting frame:** `campaign/crash-library/05-no-lights.png`

> The 13-year-old boy in the purple helmet continues his startled swerve away from the approaching car. The bike wobbles violently to one side, his foot starts to come off the pedal to catch himself, the bike's frame leans further. The car's headlights remain bright behind him; the car is clearly braking and beginning to swerve slightly to give him room. The boy's eyes stay wide with cartoon shock, mouth open. In the final fraction of a second, his outstretched foot is just about to touch the asphalt to stop the bike — frozen exactly before contact. The bike has not crashed. The car has not hit him. Twilight purple sky, warm amber streetlight overhead, suburban setting. Photorealistic candid iPhone footage at dusk. Audio: car engine passing close behind, a long sustained HORN, the boy's startled preteen 'WHOA WHOA WHOA,' chirping evening crickets in the background, cuts to silence on the freeze. NO crash, NO impact.

### Clip 06 — Wheelie Wipeout (Sora 2, 4s)

**Starting frame:** `campaign/crash-library/06-wheelie-wipeout.png`

> The 14-year-old boy in the red helmet continues to lose his battle with gravity on the red e-moto. The bike tips further past vertical. He slides further off the back of the seat with both hands still gripping the bars in cartoon-panic. His mouth widens further in the 'OH NO' face. The bike's front wheel reaches its peak height pointing nearly straight up. In the final fraction of a second, the bike has just released from his grip and he is mid-fall toward the lush green grass behind him — frozen at the apex of the launch, suspended in air. NO landing yet. Bright midday sunlight, grass roadside, slight motion blur on the spinning rear wheel. Photorealistic candid iPhone footage. Audio: rising whine of the e-moto motor at full throttle, then the sudden engine-cut as he loses contact with the bike, the boy's slow-motion-stretched preteen 'OHHHH NOOOO,' freezing into silence on the apex. NO ground impact.

---

## How to fire all six next session

After Claude Code restart, in this folder:

> *"Generate the six middle-school crash clips from `campaign/crash-library/` using fal-ai Sora 2 image-to-video, 4s each, 9:16, 720p. If Sora 2 flags any of them, immediately fall back to Kling 2.5 Turbo Pro for that one."*

I'll submit all 6 jobs in parallel using the REST upload pattern (per `fal-mcp-workflow` — file_path doesn't work on HTTP transport, and these keyframes are 0.7–3.5 MB so base64-via-data won't work either). Outputs land in `campaign/videos/`. Typical wall time: ~5–7 minutes total.

## Cost estimate

6 clips × 4s × Sora 2 standard 720p ≈ **$10–20 total**. Switching any single clip to Kling fallback drops that clip's cost to roughly half.

## Editor finish-up per clip

Each of the 6 final clips will need:
1. Hard cut at the AI-clip's last frame into the live recovery footage (a real Batavia middle schooler delivering the paired tag line)
2. End-card overlay matching the landing-page typography (Bagel Fat One display + JetBrains Mono for any data) — same template as Ep 10 `ep10-mom-jail/PRODUCTION.md`
3. CTA on the end card: `bataviail.gov/e-mobility-guide`

## A note on the model split for keyframe sourcing

Keyframes 01, 03, 05 came from **nano-banana** (Gemini 3 Pro Image). 02, 04, 06 came from **openai-images** (gpt-image-2). Both styles read as authentic phone-footage; gpt-image-2 leans slightly more cinematic, nano-banana leans slightly more documentary. Either model works as a Sora 2 input frame because Sora 2 only cares about the pixels, not the source.
