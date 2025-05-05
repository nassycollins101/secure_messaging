
import base64
import os
import hmac
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

MASTER_KEY = b"supersecretmasterkey_used_to_derive_per_user_key"

def derive_user_key(user_id: str) -> bytes:
    return hmac.new(MASTER_KEY, user_id.encode(), hashlib.sha256).digest()

def encrypt_message(plaintext: str, key: bytes) -> str:
    iv = os.urandom(16)
    padder = padding.PKCS7(128).padder()
    padded = padder.update(plaintext.encode()) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    ct = encryptor.update(padded) + encryptor.finalize()

    return base64.b64encode(iv + ct).decode()

def decrypt_message(encrypted_b64: str, key: bytes) -> str:
    raw = base64.b64decode(encrypted_b64)
    iv = raw[:16]
    ct = raw[16:]

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    padded = decryptor.update(ct) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    return (unpadder.update(padded) + unpadder.finalize()).decode()
