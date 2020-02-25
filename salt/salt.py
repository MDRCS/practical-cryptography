
import os
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend

"""The problem solved by salt is that sometimes passwords like "password,12345,.." are known as the weakest passwords and sadly they are used so much in social media
accounts so when someone could hack or get access to passwords in this kind of applications he could hash this list of passwords and search for the equivalent in the website
database, this is why salt is a good strategy to camouflage the hash by adding a random number to the hash so that it's not visible ar all"""

#Fortunately for you, recommended parameters are available.
# The r parameter should be 8, and the p parameter should be 1.
# The n parameter can vary based on whether you are doing something
# like a web site that needs to give a relatively prompt response
# or something more securely stored that does not need quick responsiveness.
# Either way, it must be a power of 2. For the interactive logins,
# 2**14 is recommended. For the more sensitive files, a number as high as 2**20 is better.

salt = os.urandom(16)
kdf = Scrypt(salt=salt,length=32,n=2**14,r=8,p=1,backend=default_backend()) #length how many Bytes content the key (ex: 32 bytes)

key = kdf.derive(b"my great password") #Binary string

kdf = Scrypt(salt=salt,length=32,n=2**14,r=8,p=1,backend=default_backend())
kdf.verify(b"my great password",key)

print("Success! (Exception if mismatch)")
