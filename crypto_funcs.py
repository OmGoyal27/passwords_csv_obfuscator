import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util.Padding import pad, unpad

# --- Helper functions ---

def _derive_key(password: str) -> bytes:
    """Derive a 32-byte AES key from a password using SHA-256"""
    return hashlib.sha256(password.encode()).digest()

def encrypt(text: str, password: str) -> str:
    key = _derive_key(password)
    iv = Random.get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(text.encode(), AES.block_size))
    return base64.b64encode(iv + ciphertext).decode('utf-8')

def decrypt(enc_text: str, password: str) -> str:
    key = _derive_key(password)
    raw = base64.b64decode(enc_text)
    iv = raw[:16]
    ciphertext = raw[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    try:
        decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return decrypted.decode('utf-8')
    except (ValueError, KeyError) as e:
        print("Decryption failed:", e)
        return None

# --- Example usage ---
if __name__ == "__main__":
    text = "OmGoyal"
    password = "Hello World"

    enc = encrypt(text, password)
    print("Encrypted:", enc)

    dec = decrypt(enc, "blakd")
    print("Decrypted:", dec)
