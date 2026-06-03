#!/usr/bin/env python3
"""Upload Benny_Video_V3.mp4 to Cloudinary and delete the scratch clip.
Same signed-upload approach as upload_videos.py."""
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

man = json.load(open(OUT))

# 1) upload Benny
pid = "batavia/clip-benny"
ts = int(time.time())
p = {"public_id": pid, "timestamp": ts, "overwrite": "true"}
data = {**p, "signature": sign(p), "api_key": API_KEY}
path = os.path.join(ROOT, "assets", "0-final-videos", "Benny_Video_V3.mp4")
with open(path, "rb") as fh:
    r = requests.post(f"https://api.cloudinary.com/v1_1/{CLOUD}/video/upload",
                      data=data, files={"file": fh}, timeout=900)
print("benny upload:", r.status_code)
j = r.json()
print("  ", j.get("secure_url"))
man["benny"] = {"file": "Benny_Video_V3.mp4", "public_id": j["public_id"],
                "secure_url": j["secure_url"], "duration": j.get("duration"),
                "width": j.get("width"), "height": j.get("height"),
                "bytes": j.get("bytes"), "version": j.get("version")}

# 2) delete scratch clip
sp = "batavia/clip-refined-courage-silk-20260603-v1"
ts2 = int(time.time())
dp = {"public_id": sp, "timestamp": ts2}
d = {**dp, "signature": sign(dp), "api_key": API_KEY}
rd = requests.post(f"https://api.cloudinary.com/v1_1/{CLOUD}/video/destroy",
                   data=d, timeout=60)
print("destroy scratch:", rd.status_code, rd.json())
man.pop("refined-courage-silk-20260603-v1", None)

json.dump(man, open(OUT, "w"), indent=2)
print("manifest kids:", len(man))
