from cryptography.hazmat.primitives.ciphers import Cipher,algorithms,modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os


key = os.urandom(32)
iv = os.urandom(16)

#Remember that in CBC encryption, the algorithm combines the first plaintext block with the IV using the XOR operation before the AES operation is applied.
aescipher = Cipher(algorithms.AES(key),
                   modes.CBC(iv),
                   backend=default_backend())

AESEncryptor = aescipher.encryptor()
AESDecryptor = aescipher.decryptor()

#Make a padder/unpadder pair for 128 bit block sizes.

padder = padding.PKCS7(128).padder()
unpadder = padding.PKCS7(128).unpadder()

plaintext = [b"SHORT",
    b"MEDIUM MEDIUM MEDIUM",
    b"LONG LONG LONG LONG LONG LONG",]

ciphertext = []

for text in plaintext:
    padded_msg = padder.update(text)
    ciphertext.append(AESEncryptor.update(padded_msg))

ciphertext.append(AESEncryptor.update(padder.finalize()))

for ci in ciphertext:
    padded_message = AESDecryptor.update(ci)
    unpadded_msg = unpadder.update(padded_message)
    print("recovred : ",unpadded_msg)

print("recovered x2", unpadder.finalize())

""" The API might be more semantically aligned, this time, but the implementation is very broken and incredibly dangerous.
Before we tell you what is wrong with it, can you try and see it yourself? Are there any security principles we’ve talked about in this chapter
that we are violating? If it isn’t obvious, read on!
A Key to Hygienic IVs The problem with Listing 3-7 is that it is reusing the same key and IV for different messages.
Take a look at the constructor where the key and IV are created. Using that single key/IV pair,
the offending code re-creates encryptor and decryptor objects in every call to encrypt_message and decrypt_message.
Remember, the IV is supposed to be different each time you encrypt, preventing the same data from being encrypted to the same ciphertext! This is not optional."""
