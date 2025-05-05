### Encryption Design

- **AES-256 CBC mode** with random IV per message using `cryptography`.
- Messages are padded to 16-byte blocks, IV is prepended to ciphertext and base64 encoded.

### User Access

- Messages are stored per `user_id`. In production, authentication is required.
- IV is extracted from the first 16 bytes of decoded ciphertext.

### Spoofing Prevention

- Would use tokens to validate actual user identity. For now, we simulate basic user isolation by keying messages to user_id.

### Debug Fix

- Original decryption missed padding removal and backend declaration.
- Fixed by explicitly removing padding and adding the default backend to `Cipher`.

 

## 🔧 Implementation Summary

This project was developed in the following steps:

### 1. Project Setup
- Initialized a Flask app with JWT-based authentication.
- Created a `.env` file to store the AES key and secret key securely.

### 2. AES-256 Encryption Integration
- Used the `cryptography` library with AES in **CBC mode**.
- Each message is encrypted with a **random IV**, which is prepended to the ciphertext before storage.

### 3. Secure Message Storage
- Messages are stored in an in-memory list along with the associated username and timestamp.
- The IV is extracted during decryption to ensure correct and secure message retrieval.

### 4. JWT-Based Access Control
- Implemented login endpoint to issue JWTs.
- All message access routes require a valid JWT, and the username in the token must match the request path.

### 5. User Identity Validation
- Protected against user ID spoofing by enforcing that the `username` in the token matches the target route.
- Unauthorized requests are blocked with 401 errors.

### 6. Debug and Test
- Included a `debug_code.py` with intentionally broken decryption logic.
- Created `test_debug_code.py` and `test_app.py` to verify both encryption/decryption and API functionality.

### 7. Optional Enhancements
- Added logic to expire messages older than 10 minutes.
- Used `curl` to manually test endpoints and verify JWT-protected access.
===========