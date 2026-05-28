---
name: cta-card
description: Bake a "DID YOU KNOW?" end card / CTA card for a Batavia "Roll Smart, Ride Safe" episode by editing the canonical Hadley template with a kid's Pixar portrait, label, tip text, and side character. Use when someone wants to make an end card, CTA card, or closing tip card for an episode.
---

Bake the "DID YOU KNOW?" end card (a.k.a. CTA card) that closes each Batavia "Roll Smart, Ride Safe" episode. You do this by editing the canonical template — it carries the entire visual system (typography, washi tape, stamp, tip box, CTA pill) — and swapping only the photo, label, tip text, and side character.

**Prerequisite:** the kid's Pixar portrait must already exist at `generated_imgs/pixar-<name>.png`. If it doesn't, run the **`pixar-character`** skill first.

## Inputs you need

1. **`generated_imgs/pixar-<name>.png`** — the kid's Pixar portrait (from the `pixar-character` skill).
2. **The kid's name** and a **short wry tag** for the polaroid label (≤ ~25 chars total, e.g. "Tyler — helmet hair").
3. **The episode's rule** under `Ord. 2026-010` and the **one-line takeaway** that echoes the kid's relief line. See the `end-card-did-you-know-pairing` and `campaign-voice-relief-reflection` memories for tone — relief-reflection, NOT snark.
4. **Which side character** appears: Officer Webb / Officer Webb + River / Matt / Lori. Use **Webb + River any time River is in the video**. Pick a **fresh pose** — vary it on every card; if reusing a character, name the prior pose and ask for a different one.

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

## Writing the label & tip box

- **Polaroid label:** `[Name] — [short wry tag]`, ≤ ~25 chars. Voice is relief-reflection (the kid is glad they learned the rule) — not snark, not a Judy-style "anyway, try my pancakes" cadence.
- **Tip box:** Paragraph 1 cites the rule under `Ord. 2026-010` in plain language. Paragraph 2 is the kid-friendly takeaway that echoes the relief line. Keep both short — the box auto-wraps and overflow eats into the side character.

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
