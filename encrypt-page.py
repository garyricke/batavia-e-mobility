#!/usr/bin/env python3
"""
Encrypt campaign-site-case.html with a password so its content cannot be read
without the password — view-source on the protected file shows only ciphertext.

Encryption: PBKDF2(SHA-256, 250k iterations) → AES-256-GCM, parameters chosen
to match the Web Crypto API decryption in protected-page-template.html.
"""

import base64
import os
import sys
from pathlib import Path

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes

ROOT = Path(__file__).parent
SRC = ROOT / "campaign-site-case.source.html"
DST = ROOT / "campaign-site-case.html"
TEMPLATE = ROOT / "protected-page-template.html"

PASSWORD = "bataviarules"
ITERATIONS = 250000
SALT_BYTES = 16
NONCE_BYTES = 12


def encrypt(plaintext: str, password: str) -> str:
    salt = os.urandom(SALT_BYTES)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=ITERATIONS,
    )
    key = kdf.derive(password.encode("utf-8"))
    nonce = os.urandom(NONCE_BYTES)
    ciphertext = AESGCM(key).encrypt(nonce, plaintext.encode("utf-8"), None)
    packed = salt + nonce + ciphertext
    return base64.b64encode(packed).decode("ascii")


def main() -> int:
    if not SRC.exists():
        print(f"Source not found: {SRC}", file=sys.stderr)
        return 1
    if not TEMPLATE.exists():
        print(f"Template not found: {TEMPLATE}", file=sys.stderr)
        return 1

    plaintext = SRC.read_text(encoding="utf-8")
    blob = encrypt(plaintext, PASSWORD)

    template = TEMPLATE.read_text(encoding="utf-8")
    out = template.replace("__CIPHERTEXT__", blob)
    out = out.replace("__ITERATIONS__", str(ITERATIONS))
    DST.write_text(out, encoding="utf-8")

    print(f"Encrypted {len(plaintext)} chars → {len(blob)} base64 chars")
    print(f"Wrote {DST}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
