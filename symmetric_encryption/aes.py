import os
from cryptography.hazmat.primitives.ciphers import Cipher,algorithms,modes
from cryptography.hazmat.backends import default_backend

"""ECB Is Not for Me Be warned, relying on ECB mode for security is irresponsibly dangerous
and it should never be used. Think of it as being good for testing and educational purposes only.
Please, don’t ever use it in your applications or projects! Seriously. You have been warned.
 Don’t make us come over there."""



# generate the random bytes string -> AES key
# that’s all it takes! An AES key is just random bits: 128 of them (16 bytes’ worth) in this example. This will allow us to use AES-128.
key = os.urandom(16)

cipherAES = Cipher(algorithms.AES(key),
                     modes.ECB(),
                     backend=default_backend())

""" AES has several modes of operation that allow us to achieve different cryptographic properties:
Electronic code book (ECB) (WARNING! DANGEROUS!)
Cipher block chaining (CBC)
Counter mode (CTR) """

aesEncryptor = cipherAES.encryptor()
aesDecryptor = cipherAES.decryptor()

ciphermsg = aesEncryptor.update(b'secret message  ') ## Pay attention here if you message is not 16 bytes you will get nothing from the encryptor
print("Encryption -> ",ciphermsg)

cleartext = aesDecryptor.update(ciphermsg)
print("Decryption -> ",cleartext)

