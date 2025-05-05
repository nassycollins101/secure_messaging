from debug_code import broken_decrypt
from crypto_utils import encrypt_message, AES_KEY

def test_broken_decrypt():
    original = "Test"
    encrypted = encrypt_message(original)
    decrypted = broken_decrypt(encrypted, AES_KEY)
    assert decrypted == original, "Decryption failed"

test_broken_decrypt()
print("Test passed ✅")
