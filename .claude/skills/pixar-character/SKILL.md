---
name: pixar-character
description: Turn a real kid (or cast member) into a Pixar-style character for the Batavia "Roll Smart, Ride Safe" e-mobility campaign, starting from a video screenshot. Use when someone wants to make a Pixar portrait, "pixar-ify" a kid, or create the character art that feeds an end card / CTA card.
---

Turn a screenshot of a real person into a Pixar-style character that matches the rest of the Batavia "Roll Smart, Ride Safe" campaign. The output feeds the `cta-card` skill (the end card uses this portrait as a reference image).

This is deliberately simple. Do **not** describe "Pixar" in a long prompt and do **not** upload other characters as reference images — the model already produces the campaign look from a short instruction.

## Inputs you need

1. **The screenshot** — a chest-up frame of the kid facing camera with a clear expression, saved as PNG. If the user hasn't supplied one, ask for the file path (or which episode/frame to grab).
2. **The kid's name** — for the output filename. Check `campaign-cast.md` memory or `end-cards-howto.html` if unsure of spelling.

> **Operational note (you, not the intern):** macOS Screenshot filenames contain a non-breaking space (U+202F) before AM/PM that breaks shell tools and MCP paths. If the path came from a screenshot, copy/rename it to something plain like `/tmp/kid-screencap.png` first, or glob for it instead of typing the name.

## Steps

1. Confirm the screenshot path and the kid's name.
2. Call **`nano-banana edit_image`** on the screenshot with:
   - **aspect:** `3:4`
   - **prompt:**
     ```
     Turn this kid into a Pixar character in the SAME style as the other characters. Keep their real likeness — face, hair, and whatever they're actually wearing.
     ```
3. Save the result to **`generated_imgs/pixar-<name>.png`** (lowercase name).
4. Show the result and review it against the watch-outs below.

> **If generation fails with an auth/config/quota error**, run `nano-banana get_configuration_status` to diagnose. It should report "Gemini API token is configured and ready to use." If it's not configured, the intern's `GEMINI_API_KEY` (from their `.env`) isn't reaching the tool — point them at Step 00 of `end-cards-howto.html` and don't keep retrying the image call.

## Watch out for (review every output)

- **Invented headwear** — if the kid had no helmet/hat/sunglasses in the screenshot, the model often adds one. Remove it.
- **Composition drift** — a chest-up source must stay chest-up, not zoomed to full-body or cropped to face-only.
- **Style drift** — it should read like a Pixar *feature still*, not a flat/cel-shaded cartoon, a glossy plastic toy, or a real photo with a filter. The other campaign characters in `generated_imgs/pixar-*.png` are the bar.
- **Lost likeness** — the model tends to "prettify": straightening braces, clearing freckles, generic-ing the haircut. The kid and their parent will notice. Keep it true to the source.
- **Wrong clothing** — it defaults to a plain tee. Match the actual shirt color and any logo/graphic.

## How to reprompt

Fix **one thing at a time** with `nano-banana continue_editing` rather than rewriting the whole prompt:

- Added a helmet/hat → "Remove the helmet — no headwear, just their hair."
- Too cartoony / flat → "Make it more photorealistic 3D like the other characters — soft skin shading and real lighting, not flat cartoon."
- Doesn't look like them → "Match the source photo's face more closely — keep the [freckles / round face / braces / curly hair]."
- Zoomed wrong → "Reframe to chest-up, same crop as the original photo."
- Wrong outfit → "Change the shirt to [actual color + any graphic]."
- Off in a way you can't name → re-run fresh from the screenshot rather than stacking edits; a clean start often beats five corrections.

Don't ship a "close enough" portrait.

## Next step

Once the portrait looks right, the kid is ready for the **`cta-card`** skill, which bakes the "DID YOU KNOW?" end card using `pixar-<name>.png` as the reference image.

Background and rationale live in the `end-card-visual-template` memory and `end-cards-howto.html` (Step 03).
