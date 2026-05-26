#!/usr/bin/env node
/**
 * Generate a Pixar-style character from a source photo using OpenAI gpt-image-1.
 * Usage: node generate-pixar-kid.js <source-image-path>
 */

const fs = require("fs");
const path = require("path");
const https = require("https");

// Load .env manually
const envPath = path.join(__dirname, ".env");
if (fs.existsSync(envPath)) {
  fs.readFileSync(envPath, "utf8")
    .split("\n")
    .forEach((line) => {
      const m = line.match(/^([^#=\s][^=]*)=(.*)$/);
      if (m) process.env[m[1].trim()] = m[2].trim();
    });
}

const { OpenAI } = require("openai");
const client = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

const sourceImage = process.argv[2];
if (!sourceImage || !fs.existsSync(sourceImage)) {
  console.error("Usage: node generate-pixar-kid.js <source-image-path>");
  process.exit(1);
}

const PROMPT = `Transform this photo into a Pixar 3D animated character portrait in the exact style of Pixar movies like Turning Red and Brave.
Preserve all key features: the bright magenta-red short hair, white over-ear headphones around the neck, black beaded necklace,
gray graphic t-shirt, and the silver/gray helmet held in hand. The character has a natural smile with no braces.
Render as a full upper-body Pixar 3D portrait with: large expressive eyes, smooth stylized 3D skin, warm sunny golden-hour lighting,
outdoor park or street setting with blue sky and greenery in the background.
High quality Pixar movie aesthetic — same style as the character "Morgan" from Batavia E-Mobility educational content.`;

async function main() {
  console.log(`Reading source image: ${sourceImage}`);
  const imageStream = fs.createReadStream(sourceImage);

  const { toFile } = require("openai");
  const imageFile = await toFile(imageStream, path.basename(sourceImage), { type: "image/png" });

  console.log("Sending to OpenAI gpt-image-1 image edit API...");
  const response = await client.images.edit({
    model: "gpt-image-1",
    image: imageFile,
    prompt: PROMPT,
    n: 1,
    size: "1024x1024",
  });

  const imageData = response.data[0].b64_json;
  const buffer = Buffer.from(imageData, "base64");

  const timestamp = new Date().toISOString().replace(/[:.]/g, "-");
  const outputDir = path.join(__dirname, "generated_imgs");
  const outputPath = path.join(outputDir, `pixar-kid-${timestamp}.png`);

  fs.writeFileSync(outputPath, buffer);
  console.log(`\nSaved: ${outputPath}`);
}

main().catch((err) => {
  console.error("Error:", err.message || err);
  process.exit(1);
});
