from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# WARNING! Never do this. Reusing a key/IV is irresponsible!
preshared_key = bytes.fromhex('00112233445566778899AABBCCDDEEFF')
preshared_iv = bytes.fromhex('00000000000000000000000000000000')

purchase_message = b"""
   <XML>
  <CreditCardPurchase>
  <Merchant>Acme Inc</Merchant>
  <Buyer>John Smith</Buyer>
  <Date>01/01/2001</Date>
  <Amount>$100.00</Amount>
  <CCNumber>555-555-555-555</CCNumber>
  </CreditCardPurchase>
</XML>
"""

aesContext = Cipher(algorithms.AES(preshared_key),
                    modes.CTR(preshared_iv),
                    backend=default_backend())

aesEncryptor = aesContext.encryptor()
aesDecryptor = aesContext.decryptor()

encrypted_msg = aesEncryptor.update(purchase_message)
print(encrypted_msg)

# bytes_list = []
# for msg,encmsg in zip(purchase_message,encrypted_msg):
#     bytes_list.append(msg ^ encmsg)

