import sys

from cryptography.hazmat.primitives.ciphers import Cipher,algorithms,modes
from cryptography.hazmat.backends import default_backend

""""We’ll encrypt this message under the key we set out previously.
 We need to pad the message to make sure it is a multiple of 16 bytes long.
 We can do that by adding extra characters to the end until its length is a multiple of 16"""
#Padding is tweaking the message till we acheive 16 bytes

key = bytes.fromhex('00112233445566778899AABBCCDDEEFF')

AESCipher = Cipher(algorithms.AES(key),
                   modes.ECB(),
                   backend=default_backend())

AESEncryptor = AESCipher.encryptor()
AESDecryptor = AESCipher.decryptor()

message = b"""
  FROM: FIELD AGENT ALICE
  TO: FIELD AGENT BOB
  RE: Meeting
  DATE: 2001-1-1

  Meet me today at the docks at 2300."""

#Measure how many bytes in a bytes object 'message'
print(sys.getsizeof(message))

#Adding some padding to acheive 16 bytes standard of the update method of aesecryptor
message += b"E" * (-len(message) % 16)
print(sys.getsizeof(message))

print(message)
ciphermsg = AESEncryptor.update(message)

print(ciphermsg)

