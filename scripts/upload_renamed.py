#!/usr/bin/env python3
"""Upload renamed videos (Janaeah, Shanel) to new public_ids and delete the old
clip-janaya / clip-chanel assets."""
import os, re, time, json, hashlib
import requests

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, ".cloudinary-videos.json")

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

def upload(fname, slug):
    pid = f"batavia/clip-{slug}"
    ts = int(time.time())
    p = {"public_id": pid, "timestamp": ts, "overwrite": "true", "invalidate": "true"}
    data = {**p, "signature": sign(p), "api_key": API_KEY}
    path = os.path.join(ROOT, "assets", "0-final-videos", fname)
    with open(path, "rb") as fh:
        r = requests.post(f"https://api.cloudinary.com/v1_1/{CLOUD}/video/upload",
                          data=data, files={"file": fh}, timeout=900)
    j = r.json()
    print(f"{slug}: {r.status_code} {j.get('secure_url')}")
    return j

def destroy(slug):
    pid = f"batavia/clip-{slug}"
    ts = int(time.time())
    p = {"public_id": pid, "timestamp": ts, "invalidate": "true"}
    data = {**p, "signature": sign(p), "api_key": API_KEY}
    r = requests.post(f"https://api.cloudinary.com/v1_1/{CLOUD}/video/destroy", data=data, timeout=60)
    print(f"destroy {slug}: {r.status_code} {r.json()}")

man = json.load(open(OUT))
for fname, slug in [("Janaeah_Video_V2.mp4", "janaeah"), ("Shanel_Video_V2.mp4", "shanel")]:
    j = upload(fname, slug)
    man[slug] = {"file": fname, "public_id": j["public_id"], "secure_url": j["secure_url"],
                 "duration": j.get("duration"), "width": j.get("width"),
                 "height": j.get("height"), "bytes": j.get("bytes"), "version": j.get("version")}

for slug in ["janaya", "chanel"]:
    destroy(slug)
    man.pop(slug, None)

json.dump(man, open(OUT, "w"), indent=2)
print("manifest kids:", len(man))
print("JANAEAH_VER", man["janaeah"]["version"])
print("SHANEL_VER", man["shanel"]["version"])
