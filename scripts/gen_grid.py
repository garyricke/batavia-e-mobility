#!/usr/bin/env python3
import os, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
man = json.load(open(os.path.join(ROOT, ".cloudinary-videos.json")))
CLOUD = "dsbllwpbh"
base = f"https://res.cloudinary.com/{CLOUD}/video/upload"
tilts = ["-2.2deg","1.5deg","-1.2deg","2deg","-1.8deg","1.2deg","-2deg","1.8deg"]

names = sorted(man.keys())  # alphabetical
cards = []
for i, slug in enumerate(names):
    v = man[slug]
    ver = f"v{v['version']}"
    pid = v["public_id"]               # batavia/clip-<slug>
    name = slug.capitalize()
    full = f"{base}/{ver}/{pid}.mp4"
    prev = f"{base}/q_auto,w_640/{ver}/{pid}.mp4"
    post = f"{base}/so_0,q_auto,w_640/{ver}/{pid}.jpg"
    dl   = f"{base}/fl_attachment:{name}-Roll-Smart-Ride-Safe/{ver}/{pid}.mp4"
    num = f"{i+1:02d}"
    r = tilts[i % len(tilts)]
    cards.append(f'''      <figure class="watch-card reveal" style="--r:{r}">
        <button type="button" class="watch-card__open" data-video="{full}" aria-label="Watch {name}'s video with sound">
          <span class="watch-card__num" aria-hidden="true">{num}</span>
          <span class="watch-card__media">
            <video src="{prev}" poster="{post}" muted loop playsinline preload="none"></video>
            <span class="watch-card__play" aria-hidden="true"></span>
          </span>
          <span class="watch-card__caption"><strong>{name}</strong></span>
        </button>
        <a class="watch-card__dl" href="{dl}" aria-label="Download {name}'s video in high quality to share">
          <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v12"/><path d="m7 11 5 5 5-5"/><path d="M5 21h14"/></svg>
          <span>Download HQ</span>
        </a>
      </figure>''')

print('\n'.join(cards))
