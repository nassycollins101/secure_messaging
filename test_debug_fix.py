from debug_code import fixed_decrypt
from crypto_utils import encrypt_message, SECRET_KEY

def test_fixed_decrypt():
    original = "Secret Debug Message"
    encrypted = encrypt_message(original)
    decrypted = fixed_decrypt(encrypted, SECRET_KEY)
    assert decrypted == original
    print("✅ Debug test passed.")

if __name__ == '__main__':
    test_fixed_decrypt()
