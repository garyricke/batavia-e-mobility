---
name: cta-card
description: Bake a "DID YOU KNOW?" end card / CTA card for a Batavia "Roll Smart, Ride Safe" episode by editing the canonical Hadley template with a kid's Pixar portrait, label, tip text, and side character. Use when someone wants to make an end card, CTA card, or closing tip card for an episode.
---

Bake the "DID YOU KNOW?" end card (a.k.a. CTA card) that closes each Batavia "Roll Smart, Ride Safe" episode. You do this by editing the canonical template — it carries the entire visual system (typography, washi tape, stamp, tip box, CTA pill) — and swapping only the photo, label, tip text, and side character.

**Prerequisite:** the kid's Pixar portrait must already exist at `generated_imgs/pixar-<name>.png`. If it doesn't, run the **`pixar-character`** skill first.

## Inputs

**The intern gives you:**
1. **The kid's name.**
2. **The video transcript** (or script) for the episode.
3. **Which side character** to use — Officer Webb / Officer Webb + River / Matt / Lori — **and the pose** they want. (Use Webb + River any time River is in the video. Remind them to vary the pose from previous cards.)
4. **`generated_imgs/pixar-<name>.png`** — the Pixar portrait (from the `pixar-character` skill). If it doesn't exist, run that skill first.

**You (Claude) derive from the transcript:**
- **The polaroid line** — a short, wry relief-reflection tag for the label, format `[Name] — [tag]`, ≤ ~25 chars total (e.g. "Tyler — helmet hair"). It should reflect what the kid actually learned in *this* episode. Voice is relief-reflection, never snark — see the `campaign-voice-relief-reflection` memory.
- **The ordinance tip** — read the transcript, identify which rule the episode is about, then pick the **best-matching fact** from the landing page `index.html` (the canonical Ordinance 2026-010 source in this repo). The polaroid line and the tip must cover the **same rule** (see the `end-card-did-you-know-pairing` memory). Write the tip as two parts: paragraph 1 states the rule plainly ("Under Batavia Ord. 2026-010, …"), paragraph 2 is the kid-friendly takeaway that echoes the relief line.

**Before generating, show the intern the polaroid line and the ordinance tip you picked, and confirm the side character + pose, so they can approve or adjust.** Then fill those into the prompt below.

## Steps

1. Confirm all inputs above. Fill in the bracketed values before calling the tool.
2. Call **`nano-banana edit_image`** on the template `generated_imgs/end-card-hadley.png` with the kid's portrait as a **reference image**:
   - **image:** `generated_imgs/end-card-hadley.png`
   - **reference:** `generated_imgs/pixar-<name>.png`
   - **aspect:** `9:16`
   - **resolution:** `2K`
   - **prompt:**
     ```
     Edit this end card by changing ONLY these elements. Preserve EVERYTHING else exactly — the "— ROLL SMART, RIDE SAFE" header, the navy "DID YOU KNOW?" title with soft orange offset shadow, the dotted + 45-degree diagonal hatched beige background, the pink/yellow washi tape, the polaroid frame, the navy-bordered light-blue tip box styling, the circular distressed "CITY OF BATAVIA · E-MOBILITY" stamp, and the yellow-orange CTA pill button shape with "MORE TIPS AT" label.

     Changes:

     1) Polaroid PHOTO — replace with the supplied reference image of [NAME]: [BRIEF DESCRIPTION — hair, clothing, distinguishing feature]. Crop to chest-up framing centered in the polaroid window.

     2) Polaroid handwritten marker label — change to "[NAME] — [SHORT WRY TAG]". Same chunky handwritten marker font, same navy color, same tilt.

     3) Tip box body text — replace with:
        Paragraph 1: "Under Batavia Ord. 2026-010, [the rule for this episode]."
        Paragraph 2 (bolder takeaway): "[the one-line takeaway that ties to the relief line]."

     4) Side character cutout in the lower-left — replace with [Officer Webb / Officer Webb + River / Matt / Lori] in a [DESCRIBE THE POSE] pose. Keep the same white sticker-outline treatment, same approximate size and position. [If reusing a side character, name the prior pose and ask for a different one.]

     5) CTA URL — keep "bataviail.gov →" exactly as is.
     ```
3. Save the final to **`generated_imgs/end-card-<name>.png`**.
4. Review against the watch-outs and the shipped cards, then flag for Gary's review before the episode ships.

## Writing the label & tip well

- **Polaroid label:** `[Name] — [short wry tag]`, ≤ ~25 chars. Relief-reflection voice (the kid is glad they learned the rule) — not snark, not a Judy-style "anyway, try my pancakes" cadence. Look at the shipped cards for the right tone.
- **Tip box:** keep both paragraphs short — the box auto-wraps and overflow eats into the side character. Surface the specific ordinance detail (age, distance, wattage, dollar amount), and prioritize the series' highest-risk confusion areas when the transcript supports it: the e-moto ban (>750 W / >20 mph throttle), parent liability, and e-scooter 18+.

## Watch out for (review every output)

- **Hair color drift** — the model sometimes darkens blondes. Re-prompt with the hair color emphasized if it shifts.
- **Doubled accessories** — two sets of headphones, two helmets. Specify "ONE set" explicitly if it happens.
- **Garbled text** — the CTA pill must read `bataviail.gov →`. Badges and stamp text must be clean. If anything is misspelled, retry.
- **Side-character drift** — wrong character or wrong pose. Retry naming the character explicitly.
- **River anatomy** — River is female. If the K9 version shows male anatomy, re-prompt: "clean smooth underbody, female dog, no visible anatomy."
- **Doesn't belong in the set** — compare against `end-card-hadley.png`, `end-card-sammy.png`, `end-card-johnny.png`, `end-card-levi.png`, `end-card-tyler.png` for typography, layout, color, polish. If it doesn't feel like it belongs, don't ship it — retry.

## The short list

- Check the cast sheet (`campaign-cast.md`) if unsure of a name.
- Use Webb & River any time River is in the video; River is female.
- Vary the side-character pose on every card.
- Confirm the CTA reads `bataviail.gov →`.
- Ship the card, then ping Gary for review before the episode goes out.

Full reference: `end-cards-howto.html` (Step 04) and the `end-card-visual-template` memory.
