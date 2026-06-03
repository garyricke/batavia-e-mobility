#!/usr/bin/env python3
"""Upload the 4 crew Pixar portraits to Cloudinary as images (batavia/crew-*)."""
import os, re, time, hashlib
import requests

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = {}
with open(os.path.join(ROOT, ".env")) as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1); env[k.strip()] = v.strip()
m = re.match(r"cloudinary://([^:]+):([^@]+)@(.+)", env["CLOUDINARY_URL"])
API_KEY, API_SECRET, CLOUD = m.group(1), m.group(2), m.group(3)

def sign(p):
    return hashlib.sha1(("&".join(f"{k}={p[k]}" for k in sorted(p)) + API_SECRET).encode()).hexdigest()

jobs = [
    ("generated_imgs/pixar-webb-river.png", "batavia/crew-webb-river"),
    ("generated_imgs/pixar-matt.png",       "batavia/crew-matt"),
    ("generated_imgs/pixar-lori.png",       "batavia/crew-lori"),
    ("generated_imgs/pixar-jack.png",       "batavia/crew-jack"),
]
for path, pid in jobs:
    ts = int(time.time())
    p = {"public_id": pid, "timestamp": ts, "overwrite": "true"}
    data = {**p, "signature": sign(p), "api_key": API_KEY}
    with open(os.path.join(ROOT, path), "rb") as fh:
        r = requests.post(f"https://api.cloudinary.com/v1_1/{CLOUD}/image/upload",
                          data=data, files={"file": fh}, timeout=300)
    j = r.json()
    print(pid, r.status_code, j.get("secure_url"), f"{j.get('width')}x{j.get('height')}")
