# THIS IS NOT SECURE. DO NOT USE THIS!!!
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os, hashlib

class Encryptor:
    
    """"Recall that “counter mode” requires no padding and that in our previous examples the “finalize” functions really didn’t do much.
     But now, when we finalize our manager, it not only finalizes encryption, it also returns the computed hash as the last few bytes to be
      appended to the encrypted data. Thus, the final encrypted message has our simple MAC tacked onto the end of it."""

    def __init__(self, key, nonce):
        aesContext = Cipher(algorithms.AES(key),
                            modes.CTR(nonce),
                            backend=default_backend())
        self.encryptor = aesContext.encryptor()
        self.hasher = hashlib.sha256()

    def update_encryptor(self, plaintext):
        ciphertext = self.encryptor.update(plaintext)
        self.hasher.update(ciphertext)
        return ciphertext

    def finalize_encryptor(self):
        return self.encryptor.finalize() + self.hasher.digest()

key = os.urandom(32)
nonce = os.urandom(16)
manager = Encryptor(key, nonce)
ciphertext = manager.update_encryptor(b"Hi Bob, this is Alice!")
ciphertext += manager.finalize_encryptor()

# Begin auto test
encryptor = Encryptor(key, nonce)
test_message = b"test message"
ciphertext = encryptor.update_encryptor(test_message)
mac = encryptor.finalize_encryptor() #We don't use padding but finilize return the hash

if not ciphertext or ciphertext == test_message:
    print("[FAIL]")
elif mac != hashlib.sha256(ciphertext).digest():
    print("[FAIL]")
else:
    print("[PASS]")
