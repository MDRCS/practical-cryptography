from cryptography.hazmat.primitives.ciphers import Cipher,algorithms,modes
from cryptography.hazmat.backends import default_backend
import os

class EncryptionManager:

    """ CTR mode - STREAM KEY is the best choice against CBC
     and also is more easy to implement and use
      Important : you must never reuse key and iV pairs.
      doing so seriously compromises security and disappoints cryptography book authors.
       Just don’t do it. always use a new key/iV pair when encrypting anything."""

    """ Why don’t you want to reuse a key and IV pair? For CBC, we already mentioned one of the potential problems:
     if you reuse a key and IV pair, you will get predictable output for predictable headers.
      Parts of your messages that you might be inclined not to think about at all,
       because they are boilerplate or contain hidden structure, will become a liability;
        adversaries can use predictable ciphertext to learn about your keys."""

    def __init__(self):
        key = os.urandom(16)
        nonce = os.urandom(16)
        aes_context = Cipher(algorithms.AES(key),
                             modes.CTR(nonce),
                             backend=default_backend())
        self.encryptor = aes_context.encryptor()
        self.decryptor = aes_context.decryptor()

    def updateEncryptor(self,plaintext):
        return self.encryptor.update(plaintext)

    def finalizeEncryptor(self):
        return self.encryptor.finalize()

    def updateDecryptor(self,ciphertext):
        return self.decryptor.update(ciphertext)

    def finalizeDecryptor(self):
        return self.decryptor.finalize()

if __name__ == "__main__":
    manager = EncryptionManager()

    plaintext = [b"SHORT",
                 b"MEDIUM MEDIUM MEDIUM",
                 b"LONG LONG LONG LONG LONG LONG", ]

    ciphertext = []

    for text in plaintext:
        ciphertext.append(manager.updateEncryptor(text))
    ciphertext.append(manager.finalizeEncryptor())

    for cipher in ciphertext:
        print("plaintext : ",manager.updateDecryptor(cipher))
    print("plaintext : ",manager.finalizeDecryptor())

