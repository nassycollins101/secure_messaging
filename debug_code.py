from base64 import b64decode
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def broken_decrypt(encoded, key):
    try:
        data = b64decode(encoded)
        iv = data[:16]
        ciphertext = data[16:]

        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        padded = decryptor.update(ciphertext) + decryptor.finalize()

        unpadder = padding.PKCS7(128).unpadder()
        plaintext = unpadder.update(padded) + unpadder.finalize()
        return plaintext.decode()
    except Exception as e:
        return str(e)
from debug_code import broken_decrypt
from crypto_utils import encrypt_message, AES_KEY

def test_broken_decrypt():
    original = "Test message"
    encrypted = encrypt_message(original)
    decrypted = broken_decrypt(encrypted, AES_KEY)
    assert decrypted == original, "Decryption failed"

test_broken_decrypt()
print("✅ Debug decryption test passed.")
