#!/usr/bin/env python3
"""Re-upload Johnny_Video_V2.mp4 over batavia/clip-johnny (with cache invalidation)."""
import os, re, time, json, hashlib
import requests

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, ".cloudinary-videos.json")

env = {}
with open(os.path.join(ROOT, ".env")) as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
m = re.match(r"cloudinary://([^:]+):([^@]+)@(.+)", env["CLOUDINARY_URL"])
API_KEY, API_SECRET, CLOUD = m.group(1), m.group(2), m.group(3)

def sign(params):
    items = "&".join(f"{k}={params[k]}" for k in sorted(params))
    return hashlib.sha1((items + API_SECRET).encode()).hexdigest()

pid = "batavia/clip-johnny"
ts = int(time.time())
p = {"public_id": pid, "timestamp": ts, "overwrite": "true", "invalidate": "true"}
data = {**p, "signature": sign(p), "api_key": API_KEY}
path = os.path.join(ROOT, "assets", "0-final-videos", "Johnny_Video_V2.mp4")
with open(path, "rb") as fh:
    r = requests.post(f"https://api.cloudinary.com/v1_1/{CLOUD}/video/upload",
                      data=data, files={"file": fh}, timeout=900)
print("johnny upload:", r.status_code)
j = r.json()
print("  url:", j.get("secure_url"))
print("  version:", j.get("version"))

man = json.load(open(OUT))
man["johnny"] = {"file": "Johnny_Video_V2.mp4", "public_id": j["public_id"],
                 "secure_url": j["secure_url"], "duration": j.get("duration"),
                 "width": j.get("width"), "height": j.get("height"),
                 "bytes": j.get("bytes"), "version": j.get("version")}
json.dump(man, open(OUT, "w"), indent=2)
print("NEW_VERSION", j.get("version"))
