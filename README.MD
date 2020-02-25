### - By the way, do you see a pattern developing here? Sometimes the best approaches for explaining a thing are not at all suitable for using it in practice. this seems to apply particularly well to cryptography, which is one reason that we urge people to always use a well established library instead of building their own.

###We’ll encrypt this message under the key we set out previously. We need to pad the message to make sure it is a multiple of 16 bytes long. We can do that by adding extra characters to the end until its length is a multiple of 16.

###Truth tables are useful, showing precisely how functions like XOR behave for all combinations of inputs, but you actually don’t need to think about XOR at this level. What is important is that XOR has an amazing inversion property: the XOR operation is its own inverse! That is, if you start with some binary number A and XOR it with B, you can recover A by XORing the output with B again. Mathematically, it looks like this: (A⊕B)⊕B=A.

##### XOR OPERATION IN PYTHON -> 5^12 = 9 IF 12ˆ5 = 9

#####Explaining ./symmetric_encryption/padding_message_aes_ecb.py

Walking through Listing 3-6 one more time illustrates how the effects of these operations are compounded when the padder and encryptor are used together. On
the first pass through the loop for encrypting the messages, the input is SHORT. Five characters is less than of a block. The padder’s update() method does not add any padding, so the padder buffers these five characters and the update() method returns an empty byte string. When this gets passed to the encryptor, there is obviously not a full block so the encryptor’s update method also returns an empty byte string. This gets appended to the list of ciphertexts.
On our second pass through the loop, the input is MEDIUM MEDIUM MEDIUM. These 20 characters are passed into the padder’s internal buffer and are added to the 5 that were there before. The UPDATE method now returns the first 16 of those 25 bytes (a full block), leaving the remaining 9 bytes in the internal buffer. The 16 bytes from the padder are encrypted and stored in the list of ciphertexts.
In the final pass, the LONG LONG LONG LONG LONG LONG input is added to the padder’s internal buffer. These 29 bytes are added to the current 9 bytes in the buffer for a total of 38 bytes. The padder returns the 2 full blocks (of 16 bytes each) leaving the last 6 bytes in its buffer. The two blocks are encrypted, and the two-block output is stored in the list of ciphertexts.
Once the loop exits, the padder’s finalize method is called. It takes the last bytes of input, appends the necessary padding, and passes it to the encryption operation. The ciphertext is appended to the list and encryption is over. There are now four ciphertext messages to decrypt. Reversing the process, the first message is, you may recall, the empty buffer. It just passes straight through everything and comes out as an empty message.
But the next recovered text is also empty. That’s because the first full block to the unpadder is reserved for the reasons we explained. It produces an empty output fed into the AES decryptor’s update() method. This generates our second empty output.
The remaining three are more straightforward.
Now that the walk-through is finished, did you notice that we were still using the incorrect terminology? We referred to individual outputs from update() methods as individual ciphertexts rather than a snippet of the ciphertext. Similarly, we called the output of the decryptor update methods recovered texts rather than part of a single recovered message.

### - symmetric encryption - aes :
#####Accordingly, when using the API of Python’s cryptography module, never give the same key and IV pair to an encryptor more than once (obviously, you give the same key and IV to the corresponding decryptor). In fact, it’s probably best to never reuse the same key again, period.

###Key and IV managment

Why don’t you want to reuse a key and IV pair? For CBC, we already mentioned one of the potential problems: if you reuse a key and IV pair, you will get predictable output for predictable headers. Parts of your messages that you might be inclined not to think about at all, because they are boilerplate or contain hidden structure, will become a liability; adversaries can use predictable ciphertext to learn about your keys.
Think about an HTML page, for example. The first characters are often the same across multiple pages (e.g., "<!DOCTYPE html>\n"). If the first 16 bytes (an AES block) of HTML pages are the same and you encrypt them under the same key/IV pair, the ciphertext will be the same for each one. You have just leaked data to your enemy, and they can start to analyze your encrypted data for patterns.
If your web site has a large amount of static content or dynamic results that are identically generated, each encrypted page becomes uniquely identifiable. The enemy may not know what each page says, but they can determine the frequency of use and track which parties receive the same pages.
Reusing a key and IV in CBC mode is bad.
Reusing a key and IV in counter mode, on the other hand, is much worse. Because

### keystream-stealing attack $$$ - Strategy to decrypt purchase from a store **** :
For simplicity, the purchase message was included in the preceding code. Feel free to change it to accept a file or command-line flags that set the buyer’s name, purchase price, and so forth. You probably ought to also write the encrypted message to a file.
Back to our scenario, if you are trying to crack this system, you can spend $100.00 at this store, then tap the line and intercept the purchase message transmitted to the bank. If you do this, how much of the plaintext message do you know? You know all of it! You know who made the purchase, you know the amount of the purchase, you know the date, and you know your own credit card number.
That means that you can recreate the plaintext message, XOR it with the ciphertext, and recover keystream material. Because the merchant is reusing the same key and IV for the next customer, you can trivially decrypt the message and read the contents. Oops. We feel a news story about a data breach coming on.

###RSA - ASYMMETRIC ENCRYPTION

see how everything hinges on the private key in rsa? the public key is derived from it. While either key can be used to encrypt (and the other can be used to decrypt), the private key is special because of this property. rsa keys are not only asymmetric because one encrypts and the other decrypts, they are also asymmetric because you can derive an rsa public key from the private key, but not the other way around.
the private_bytes and public_bytes methods convert large integer keys into bytes that are in a standard network- and disk-ready encoding called a pem. the corresponding serialization “load” methods can be used to decode these after reading those bytes from disk so that they look like keys again to the encryption and decryption algorithms.
it is possible (and a very good idea) to encrypt the private key itself, but we opted not to do that here, which is why no password is used.


###Symmetric vs Asymmetric Encryption
In symmetric encryption, there is a single, shared key that works to both encrypt and decrypt the message. This means that anyone with the power to create an encrypted message has the same ability to decrypt the same message. It is impossible to give somebody the power to decrypt a symmetrically encrypted message without also giving them the ability to encrypt the same kind of messages and vice versa.
In asymmetric cryptography, there is always a private key that must never be disclosed and a public key that can be disclosed widely. Exactly what can be done with the key pair depends on the algorithm. In this chapter we have been focusing on RSA encryption. We’ll review RSA’s operations in this section as a concrete example but keep in mind that they may not apply to other asymmetric algorithms and operations.
Specifically, RSA supports an asymmetric encryption scheme in which you can
use one key to encrypt the message and a different key to decrypt a message. Typically, either key can act in either role: a private key can encrypt messages that can be decrypted by the public key and vice versa. With RSA, of course, one key is clearly the private key because the public key can be derived from the private key, but not the other way around. It is impossible to have an RSA private key and not also have the matching public key. Thus, one key is unambiguously designated as “private” and the other is “public.”


### An Overly Simplistic Message Authentication Code (MAC)
- this introductory and incorrect starting point. The basic idea for this overly simplistic MAC is this:
The sender computes a code C1 using a function f (M1) for a given message M1.
The sender transmits M1 and C1 to the recipient.
The recipient receives the data as M and C, but does not know if  they have been modified.
The recipient recomputes f (M) and compares the output to C to verify that the message is unaltered.
Suppose that Eve intercepts M1 and C1 sent by Alice to Bob. If Eve wants to change the message M1 to M2, she must also recompute C2 = f (M2) and send both M2 and C2 to Bob. Otherwise, Bob will detect that something has been changed because f (M) and C will not match.
