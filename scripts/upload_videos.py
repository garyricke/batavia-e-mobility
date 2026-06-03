#!/usr/bin/env python3
"""Signed upload of final squad videos to Cloudinary (cloud: dsbllwpbh).
Reads CLOUDINARY_URL from .env, uploads every mp4 in assets/0-final-videos/
as resource_type=video under public_id batavia/clip-<slug>, and writes a
manifest to .cloudinary-videos.json."""
import os, re, sys, time, json, hashlib, urllib.parse
import requests

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VID_DIR = os.path.join(ROOT, "assets", "0-final-videos")
OUT = os.path.join(ROOT, ".cloudinary-videos.json")

# --- parse CLOUDINARY_URL from .env ---
env = {}
with open(os.path.join(ROOT, ".env")) as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
m = re.match(r"cloudinary://([^:]+):([^@]+)@(.+)", env["CLOUDINARY_URL"])
API_KEY, API_SECRET, CLOUD = m.group(1), m.group(2), m.group(3)
print(f"cloud={CLOUD}")

def slug_for(fname):
    base = os.path.splitext(fname)[0]
    # strip "_Video"/"_video" and everything after; fall back to whole base
    parts = re.split(r"_video", base, flags=re.IGNORECASE)
    name = parts[0] if parts[0] else base
    name = re.sub(r"[^A-Za-z0-9]+", "-", name).strip("-").lower()
    return name

def sign(params):
    items = "&".join(f"{k}={params[k]}" for k in sorted(params))
    return hashlib.sha1((items + API_SECRET).encode()).hexdigest()

results = {}
files = sorted(f for f in os.listdir(VID_DIR) if f.lower().endswith(".mp4"))
print(f"{len(files)} videos to upload")
for i, fname in enumerate(files, 1):
    slug = slug_for(fname)
    public_id = f"batavia/clip-{slug}"
    ts = int(time.time())
    params = {"public_id": public_id, "timestamp": ts, "overwrite": "true"}
    sig = sign(params)
    data = {**params, "api_key": API_KEY, "signature": sig}
    path = os.path.join(VID_DIR, fname)
    mb = os.path.getsize(path) / 1e6
    print(f"[{i}/{len(files)}] {fname} ({mb:.1f}MB) -> {public_id} ...", flush=True)
    with open(path, "rb") as fh:
        r = requests.post(
            f"https://api.cloudinary.com/v1_1/{CLOUD}/video/upload",
            data=data, files={"file": fh}, timeout=900)
    if r.status_code != 200:
        print(f"   FAILED {r.status_code}: {r.text[:300]}", flush=True)
        results[slug] = {"error": r.text[:300], "file": fname}
        continue
    j = r.json()
    results[slug] = {
        "file": fname,
        "public_id": j["public_id"],
        "secure_url": j["secure_url"],
        "duration": j.get("duration"),
        "width": j.get("width"),
        "height": j.get("height"),
        "bytes": j.get("bytes"),
        "version": j.get("version"),
    }
    print(f"   OK {j['secure_url']}", flush=True)
    with open(OUT, "w") as out:
        json.dump(results, out, indent=2)

with open(OUT, "w") as out:
    json.dump(results, out, indent=2)
print(f"\nDone. Manifest -> {OUT}")
