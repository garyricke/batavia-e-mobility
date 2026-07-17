#!/usr/bin/env python3
"""
Encrypt engagement-report.source.html into engagement-report.html so the report
content (resident comments, analysis) is ciphertext in the public repo — only a
password unlocks it in the browser. Same AES-256-GCM / PBKDF2 scheme as
encrypt-page.py, matching protected-page-template.html's Web Crypto decryption.

Workflow:
    # edit / regenerate the plaintext engagement-report.source.html (gitignored)
    python3 encrypt-report.py
    git add engagement-report.html && git commit && git push
"""

import base64
import os
import sys
from pathlib import Path

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes

ROOT = Path(__file__).parent
SRC = ROOT / "engagement-report.source.html"
DST = ROOT / "engagement-report.html"
TEMPLATE = ROOT / "protected-page-template.html"

PASSWORD = "wecare"
ITERATIONS = 250000
SALT_BYTES = 16
NONCE_BYTES = 12

# Report-specific lock-screen copy (leaves the shared template file untouched)
ORIG_SUB = ("This page is a private proposal for City of Batavia staff. "
            "Enter the password Gary shared with you to view it.")
NEW_SUB = ("This is a private engagement report for City of Batavia staff. "
           "Enter the password Gary shared with you to view it.")
ORIG_TITLE = ">Password <span class=\"accent\">required.</span></h1>"
NEW_TITLE = ">Engagement <span class=\"accent\">report.</span></h1>"


def encrypt(plaintext: str, password: str) -> str:
    salt = os.urandom(SALT_BYTES)
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=ITERATIONS)
    key = kdf.derive(password.encode("utf-8"))
    nonce = os.urandom(NONCE_BYTES)
    ciphertext = AESGCM(key).encrypt(nonce, plaintext.encode("utf-8"), None)
    return base64.b64encode(salt + nonce + ciphertext).decode("ascii")


def main() -> int:
    for p in (SRC, TEMPLATE):
        if not p.exists():
            print(f"Missing: {p}", file=sys.stderr)
            return 1
    plaintext = SRC.read_text(encoding="utf-8")
    blob = encrypt(plaintext, PASSWORD)
    tpl = TEMPLATE.read_text(encoding="utf-8")
    tpl = tpl.replace(ORIG_SUB, NEW_SUB).replace(ORIG_TITLE, NEW_TITLE)
    out = tpl.replace("__CIPHERTEXT__", blob).replace("__ITERATIONS__", str(ITERATIONS))
    DST.write_text(out, encoding="utf-8")
    print(f"Encrypted {len(plaintext)} chars -> {len(blob)} base64 chars")
    print(f"Wrote {DST} (password: {PASSWORD})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
