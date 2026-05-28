# Setup — End-Card Workflow

One-time setup on a new machine. Takes ~5 minutes. After this, making an end card is just talking to Claude Code (see `end-cards-howto.html`).

## What you need first

1. **Claude Code** installed — https://claude.com/claude-code
2. **Node.js 18+** installed — https://nodejs.org (the image tool runs through it)
3. **The `.env` file** you were given from Gary. Drop it in the root of this project folder. It holds the API keys and is never committed to git.

## Run the setup

From the project folder, in a terminal:

```bash
bash scripts/setup.sh
```

This reads the Gemini key from your `.env` and connects the image tool (**nano-banana**) to Claude Code. You only do this once per machine. It's safe to re-run.

## Confirm it worked

1. Fully quit and reopen Claude Code.
2. Type:

   ```
   check my nano-banana setup
   ```

3. You should see **"Gemini API token is configured and ready to use."**

If it says it's *not* configured, make sure `.env` is in this folder and has a `GEMINI_API_KEY=` line, restart Claude Code, and re-run `bash scripts/setup.sh`. Still stuck? Send Gary what Claude printed.

## Now make a card

Open `end-cards-howto.html` in a browser and follow it. The short version:

- *"make a Pixar character from this screenshot of [name]"*
- *"make the end card for [name]"*

Claude picks the right skill and walks you through the rest.
