#!/usr/bin/env python3
"""
Upload the four case-document character images to Cloudinary under
batavia/, then write/merge the results into .cloudinary-uploads.json.

Run from the project root with credentials in the environment:

    export CLOUDINARY_API_KEY=...
    export CLOUDINARY_API_SECRET=...
    # CLOUDINARY_CLOUD_NAME defaults to dsbllwpbh
    python3 upload-case-images.py

No external dependencies — uses urllib + hashlib only.
"""

from __future__ import annotations

import hashlib
import json
import mimetypes
import os
import sys
import time
import uuid
from pathlib import Path
from typing import Any
from urllib import request, error

ROOT = Path(__file__).parent
MANIFEST = ROOT / ".cloudinary-uploads.json"

CLOUD = os.environ.get("CLOUDINARY_CLOUD_NAME", "dsbllwpbh")
KEY = os.environ.get("CLOUDINARY_API_KEY")
SECRET = os.environ.get("CLOUDINARY_API_SECRET")

# Map of source-path → desired Cloudinary public_id (under batavia/).
UPLOADS = {
    "generated_imgs/edited-2026-05-21T20-39-27-155Z-2uby45.png":
        "batavia/end-card-hadley",
    "generated_imgs/edited-2026-05-21T20-24-30-816Z-awrwlj.png":
        "batavia/end-card-josh",
    "generated_imgs/edited-2026-05-21T21-04-58-833Z-j8h7m2.png":
        "batavia/end-card-morgan",
    "generated_imgs/edited-2026-05-21T20-54-13-513Z-dnodg1.png":
        "batavia/officer-webb-finger-up",
}


def sign(params: dict[str, Any], secret: str) -> str:
    """Build a Cloudinary upload signature: sha1(sorted_params + secret)."""
    items = sorted((k, v) for k, v in params.items() if v not in (None, ""))
    payload = "&".join(f"{k}={v}" for k, v in items)
    return hashlib.sha1((payload + secret).encode("utf-8")).hexdigest()


def multipart_body(fields: dict[str, str], file_path: Path) -> tuple[bytes, str]:
    """Build a multipart/form-data body manually."""
    boundary = f"----formboundary{uuid.uuid4().hex}"
    crlf = b"\r\n"
    parts: list[bytes] = []
    for name, value in fields.items():
        parts.append(f"--{boundary}".encode())
        parts.append(f'Content-Disposition: form-data; name="{name}"'.encode())
        parts.append(b"")
        parts.append(str(value).encode("utf-8"))
    parts.append(f"--{boundary}".encode())
    parts.append(
        f'Content-Disposition: form-data; name="file"; filename="{file_path.name}"'.encode()
    )
    mime, _ = mimetypes.guess_type(file_path.name)
    parts.append(f"Content-Type: {mime or 'application/octet-stream'}".encode())
    parts.append(b"")
    parts.append(file_path.read_bytes())
    parts.append(f"--{boundary}--".encode())
    parts.append(b"")
    body = crlf.join(parts)
    return body, f"multipart/form-data; boundary={boundary}"


def upload(file_path: Path, public_id: str) -> dict[str, Any]:
    timestamp = int(time.time())
    signed_params = {
        "public_id": public_id,
        "timestamp": timestamp,
        "overwrite": "true",
        "invalidate": "true",
    }
    signature = sign(signed_params, SECRET)
    fields = {
        **{k: str(v) for k, v in signed_params.items()},
        "api_key": KEY,
        "signature": signature,
    }
    body, content_type = multipart_body(fields, file_path)
    url = f"https://api.cloudinary.com/v1_1/{CLOUD}/image/upload"
    req = request.Request(url, data=body, headers={"Content-Type": content_type})
    try:
        with request.urlopen(req, timeout=120) as resp:
            payload = json.loads(resp.read())
    except error.HTTPError as e:
        msg = e.read().decode("utf-8", errors="replace")
        raise SystemExit(f"Cloudinary upload failed ({e.code}): {msg}")
    return payload


def main() -> int:
    if not KEY or not SECRET:
        print("Set CLOUDINARY_API_KEY and CLOUDINARY_API_SECRET first.", file=sys.stderr)
        return 1

    manifest: dict[str, Any] = {}
    if MANIFEST.exists():
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    for rel_src, public_id in UPLOADS.items():
        src = ROOT / rel_src
        if not src.exists():
            print(f"  ✗ missing: {rel_src}", file=sys.stderr)
            continue
        print(f"  ↑ {src.name}  →  {public_id}")
        resp = upload(src, public_id)
        slug = public_id.split("/", 1)[-1]
        manifest[slug] = {
            "url": resp["secure_url"],
            "public_id": resp["public_id"],
            "width": resp.get("width"),
            "height": resp.get("height"),
            "bytes": resp.get("bytes"),
        }
        print(f"     {resp['secure_url']}")

    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"\nManifest updated: {MANIFEST.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
