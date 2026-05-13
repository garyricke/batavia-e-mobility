# Episode 1 — "Geese Got Me" · Production Package

**Total target runtime:** ~16 seconds (vertical 9:16)
**Rule it teaches:** Helmet required for anyone under 16 on any e-mobility device.

---

## The 5-frame storyboard (AI crash half — 0:00–0:06)

| # | File | Beat | Time |
|---|---|---|---|
| 1 | `frame-1-peaceful.png` | Boy happily rides e-bike past pond. Geese visible, calm. | 0:00–0:01 |
| 2 | `frame-2-trigger.png` | Geese begin to lift off; boy hasn't noticed. | 0:01–0:02 |
| 3 | `frame-3-launch.png` | Low-angle launch. Boy sees them. "O" face. | 0:02–0:03 |
| 4 | `frame-4-chaos.png` | Total feather-and-goose tornado peak. | 0:03–0:05 |
| 5 | `frame-5-aftermath.png` | Empty path. Single feather falling. Rubber duck bell tipped on its side. | 0:05–0:06 |

**The cut:** Hard cut from `frame-5-aftermath.png` to the live recovery shot.

## The recovery composition reference (live half — 0:06–0:14)

`recovery-reference.png` is a **photoreal cinematic reference** — *not* an asset to use in the final edit. Hand it to your DP / director of photography. It locks:

- **Framing:** eye-level, subject in lower-center third, vertical 9:16
- **Lighting:** golden hour, soft warm Midwestern sunlight, long shadows
- **Color grade:** Arri Alexa warm filmic, slight film grain
- **Lens feel:** shallow depth of field, beautifully blurred bokeh trees behind
- **Subject blocking:** cross-legged on grass, helmet on, single feather in hand, rubber goose toy on the grass beside her
- **Performance note:** calm half-smile, examining the feather. "I just survived something insane and I'm slightly bemused."

---

## Three ways to turn the storyboard into a finished video

Pick one based on your team's budget and tools. They produce roughly equivalent results.

### Option A — Image-to-video in Sora 2 / Veo 3 / Runway Gen-4 (recommended)

Each of these accepts a starting frame and a motion prompt. You generate **4 short clips** (one per transition) and stitch them.

**Clip 1 — Frame 1 → Frame 2 (1.5s)**
> Starting frame: `frame-1-peaceful.png`
>
> Prompt: *"The cartoon boy continues riding his sky-blue e-bike along the path, slow forward camera dolly. In the pond on the right, cartoon Canada geese suddenly begin lifting off the water in alarm — wings unfurling, water droplets spraying. The boy still hasn't noticed. Pixar 3D cartoon style, bright daylight, smooth cinematic motion."*

**Clip 2 — Frame 2 → Frame 3 (1.5s)**
> Starting frame: `frame-2-trigger.png`
>
> Prompt: *"Camera whips downward to a dramatic low angle. The geese explode upward out of the pond in a massive tornado-shaped swarm, wings beating, beaks honking. The boy looks up in cartoon surprise, eyes wide, mouth open in an 'O.' Helmet stays firmly on. Pixar 3D cartoon, exaggerated slapstick physics, motion lines."*

**Clip 3 — Frame 3 → Frame 4 (2s)**
> Starting frame: `frame-3-launch.png`
>
> Prompt: *"The geese tornado completely engulfs the boy and his e-bike. The bike spirals upward, feathers fill every part of the frame, geese fly chaotically around the rider. Camera holds steady on the swirling chaos. Pixar 3D cartoon, peak slapstick energy, exaggerated motion blur."*

**Clip 4 — Frame 4 → Frame 5 (1s)**
> Starting frame: `frame-4-chaos.png`
>
> Prompt: *"The cartoon chaos suddenly clears. Geese fly off into the far distance. The frame becomes still and serene. A single white goose feather drifts gently downward in the center of the frame. A small rubber duck bike bell rests tipped over on the empty path. Soft dust still swirling. Pixar 3D cartoon, sudden calm, golden daylight."*

Stitch the four clips end-to-end in CapCut, DaVinci Resolve, or Premiere. Hard cut at the end of Clip 4 into your live recovery footage. Total AI crash duration: ~6 seconds.

**Tool tip:** Sora 2 and Veo 3 are best at maintaining character consistency across the 4 clips. Runway Gen-4 and Kling 2.5 are cheaper but you'll likely need 2–3 generations per clip to get one where the helmet stays sky-blue throughout.

### Option B — Pure image-to-video on a single 6-second clip (Veo 3 Long, Sora 2)

If your tool supports 6–8s clips with motion control, generate **one** longer clip from `frame-1-peaceful.png` using the full episode-1 prompt from `video-scripts-v2.md`. Faster, but you give up some control over the precise beat-by-beat staging.

### Option C — Stitch the 5 stills into a motion video (zero AI video budget)

In DaVinci Resolve (free) or Premiere:

1. Drop the 5 frames onto the timeline with each held for **1.2s**.
2. Add a **Ken Burns** push-in on Frames 1, 2, and 5 (gentle, 4–6% scale).
3. Add a **camera shake** preset (the free "Action Shake" in Resolve) on Frames 3 and 4 — *heavy* on 4.
4. Add a **motion-blur transition** (0.3s) between each frame.
5. Drop a **feather-fall stock overlay** (free from Pixabay / Mixkit, search "feather falling green screen") across Frames 4 and 5 set to "Screen" blend mode.
6. Sound design: build the goose orchestra by layering 5–8 different honking goose stock SFX, hard-stop them on the cut to the live recovery. The silence after the chaos is what makes it funny.

This produces a perfectly serviceable 6-second crash sequence — and frankly, the rhythm of stills + sound design is often funnier than a smoothly animated version, because each beat lands as a comic-strip panel.

---

## Audio shopping list (free / low-cost)

For SFX, free libraries that won't get you copyright-struck:

- **Pixabay Music & SFX** — free, royalty-free. Search "goose honk," "feather drift," "rocket launch."
- **Mixkit Free SFX Library** — same deal.
- **Epidemic Sound** — paid but cheap, much better selection if you're producing 13 episodes.
- **Helmet click** — record this yourself once with a phone in a quiet room. You'll use it on every episode for the rest of the series. Keep it.

---

## What to deliver to whoever shoots the live half

Bundle the following in a single Dropbox/Drive folder before the shoot day:

- `recovery-reference.png` — the framing/lighting target
- `frame-5-aftermath.png` — what immediately precedes the cut, so the DP can match the camera position and lens feel
- A printout of the kid's line from `video-scripts-v2.md` (Ep 1)
- The hot-pink helmet with the yellow star sticker
- A real white feather + a rubber goose toy
- 30 minutes of golden-hour daylight on a Batavia front lawn

That is the entire shopping list for the live half. The kid does it in one take.

---

## File index

```
campaign/ep01-geese-got-me/
├── frame-1-peaceful.png        # 0:00 — establishing
├── frame-2-trigger.png         # 0:01 — geese start
├── frame-3-launch.png          # 0:02 — incoming
├── frame-4-chaos.png           # 0:03 — peak chaos
├── frame-5-aftermath.png       # 0:05 — empty path, cut frame
├── recovery-reference.png      # photoreal DP reference for the live shoot
└── PRODUCTION.md               # this file
```
