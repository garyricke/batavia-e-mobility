#!/usr/bin/env node
/**
 * Renders a "Did You Know?" end card matching the Batavia e-mobility series style.
 * Outputs to generated_imgs/end-card-frank.png
 */

const puppeteer = require("puppeteer-core");
const path = require("path");
const fs = require("fs");

const ROOT = __dirname;

function toDataUrl(filePath) {
  const data = fs.readFileSync(filePath);
  return "data:image/png;base64," + data.toString("base64");
}

const kidImg     = toDataUrl(path.join(ROOT, "generated_imgs/pixar-kid-2026-05-26T15-05-58-526Z.png"));
const officerImg = toDataUrl(path.join(ROOT, "generated_imgs/edited-2026-05-21T20-35-08-898Z-v0tnpq.png"));

const html = `<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=Caveat:wght@700&family=Nunito:wght@700;800;900&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    width: 540px;
    height: 960px;
    overflow: hidden;
    background-color: #EDE8D8;
    background-image:
      repeating-linear-gradient(
        -45deg,
        transparent,
        transparent 14px,
        rgba(160,140,100,0.13) 14px,
        rgba(160,140,100,0.13) 15px
      );
    font-family: 'Nunito', sans-serif;
  }

  .card {
    position: relative;
    width: 540px;
    height: 960px;
  }

  /* ── Header ── */
  .subheader {
    position: absolute;
    top: 28px;
    left: 0; right: 0;
    text-align: center;
    font-family: 'Nunito', sans-serif;
    font-weight: 900;
    font-size: 20px;
    letter-spacing: 2px;
    color: #1C2B55;
  }

  .main-header {
    position: absolute;
    top: 54px;
    left: 0; right: 0;
    display: flex;
    justify-content: center;
  }

  /* ── Rotation labels ── */
  .rot {
    position: absolute;
    font-family: 'Nunito', sans-serif;
    font-weight: 900;
    font-size: 17px;
    color: #1C2B55;
    z-index: 20;
  }

  /* ── Tape strips ── */
  .tape-left {
    position: absolute;
    top: 210px;
    left: 52px;
    width: 82px;
    height: 26px;
    background: #F9A8D4;
    border-radius: 3px;
    transform: rotate(-6deg);
    z-index: 12;
    opacity: 0.9;
  }

  .tape-right {
    position: absolute;
    top: 208px;
    right: 52px;
    width: 82px;
    height: 26px;
    background: #FCD34D;
    border-radius: 3px;
    transform: rotate(5deg);
    z-index: 12;
    opacity: 0.9;
  }

  /* ── Polaroid ── */
  .polaroid {
    position: absolute;
    top: 205px;
    left: 50%;
    transform: translateX(-50%) rotate(-2deg);
    background: #fff;
    padding: 13px 13px 56px;
    box-shadow: 5px 8px 28px rgba(0,0,0,0.26);
    width: 378px;
    z-index: 8;
  }

  .polaroid-photo {
    width: 352px;
    height: 326px;
    object-fit: cover;
    object-position: center 8%;
    display: block;
  }

  .polaroid-label {
    font-family: 'Caveat', cursive;
    font-weight: 700;
    font-size: 30px;
    color: #1C2B55;
    text-align: center;
    margin-top: 10px;
    line-height: 1;
  }

  /* ── Tip box ── */
  .tip-box {
    position: absolute;
    top: 624px;
    left: 14px;
    right: 14px;
    background: #C8E0F4;
    border: 2.5px solid #5A8EC2;
    border-radius: 14px;
    padding: 16px 20px 18px 150px;
    font-size: 16px;
    font-weight: 700;
    color: #1C2B55;
    line-height: 1.5;
    transform: rotate(-1.5deg);
    z-index: 2;
  }

  .tip-box strong {
    display: block;
    margin-top: 6px;
    font-weight: 900;
    font-size: 16px;
  }

  /* ── Officer ── */
  .officer {
    position: absolute;
    bottom: 100px;
    left: -8px;
    width: 165px;
    height: 255px;
    object-fit: cover;
    object-position: center top;
    z-index: 10;
  }

  /* ── Stamp ── */
  .stamp {
    position: absolute;
    bottom: 18px;
    left: 14px;
    width: 82px;
    height: 82px;
    border-radius: 50%;
    border: 2.5px solid rgba(28,43,85,0.55);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    color: rgba(28,43,85,0.55);
    text-transform: uppercase;
    z-index: 11;
    padding: 6px;
  }
  .stamp-top  { font-size: 6.5px; letter-spacing: 1.8px; font-weight: 800; }
  .stamp-mid  { font-size: 12px;  font-weight: 900; margin: 2px 0; }
  .stamp-bot  { font-size: 6px;   letter-spacing: 1.5px; font-weight: 800; }

  /* ── CTA ── */
  .cta {
    position: absolute;
    bottom: 20px;
    left: 106px;
    right: 14px;
    background: #E8A018;
    border: 3px solid #1C2B55;
    border-radius: 60px;
    padding: 12px 18px 13px;
    text-align: center;
    z-index: 11;
    box-shadow: 3px 3px 0 #1C2B55;
  }
  .cta-sub {
    display: block;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: #1C2B55;
    margin-bottom: 1px;
  }
  .cta-url {
    display: block;
    font-size: 22px;
    font-weight: 900;
    color: #1C2B55;
    letter-spacing: -0.5px;
  }
</style>
</head>
<body>
<div class="card">

  <div class="subheader">— ROLL SMART, RIDE SAFE</div>
  <div class="main-header">
    <svg viewBox="0 0 528 118" xmlns="http://www.w3.org/2000/svg" width="528" height="118">
      <text
        x="264" y="96"
        text-anchor="middle"
        font-family="Oswald, sans-serif"
        font-size="100"
        font-weight="700"
        font-style="italic"
        fill="#1C2B55"
        stroke="#E09018"
        stroke-width="8"
        paint-order="stroke fill"
        textLength="518"
        lengthAdjust="spacingAndGlyphs"
      >DID YOU KNOW?</text>
    </svg>
  </div>

  <!-- Rotation labels -->
  <div class="rot" style="top:146px; right:22px;">-2°</div>
  <div class="rot" style="top:200px; left:18px;">-6°</div>
  <div class="rot" style="top:200px; right:18px;">+5°</div>
  <div class="rot" style="top:618px; left:16px;">-4°</div>
  <div class="rot" style="top:618px; right:16px;">-1.5°</div>

  <!-- Tape -->
  <div class="tape-left"></div>
  <div class="tape-right"></div>

  <!-- Polaroid -->
  <div class="polaroid">
    <img class="polaroid-photo" src="${kidImg}" alt="Frank">
    <div class="polaroid-label">Frank &mdash; helmet hair</div>
  </div>

  <!-- Tip box -->
  <div class="tip-box">
    Under Batavia Ord. 2026-010, anyone under 16 must wear a helmet on every e-mobility device &mdash; every single ride.
    <strong>Helmet hair beats a head injury every time.</strong>
  </div>

  <!-- Officer Webb (sunglasses) -->
  <img class="officer" src="${officerImg}" alt="Officer Webb">

  <!-- Stamp -->
  <div class="stamp">
    <span class="stamp-top">City of</span>
    <span class="stamp-mid">Batavia</span>
    <span class="stamp-bot">&bull; E-Mobility &bull;</span>
  </div>

  <!-- CTA -->
  <div class="cta">
    <span class="cta-sub">More Tips At</span>
    <span class="cta-url">bataviail.gov &rarr;</span>
  </div>

</div>
</body>
</html>`;

const htmlPath = path.join(ROOT, "end-card-frank.html");
fs.writeFileSync(htmlPath, html);

(async () => {
  const browser = await puppeteer.launch({
    executablePath: "C:\\Users\\JackW\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe",
    args: ["--no-sandbox", "--disable-setuid-sandbox"],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 540, height: 960, deviceScaleFactor: 2 });
  await page.goto("file:///" + htmlPath.replace(/\\/g, "/"), { waitUntil: "networkidle0" });
  await new Promise(r => setTimeout(r, 2500));

  const outputPath = path.join(ROOT, "generated_imgs", "end-card-frank.png");
  await page.screenshot({ path: outputPath, fullPage: false });
  await browser.close();

  fs.unlinkSync(htmlPath);
  console.log("Saved:", outputPath);
})().catch(err => { console.error(err); process.exit(1); });
