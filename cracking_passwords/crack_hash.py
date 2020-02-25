import string
import hashlib
import time

def generate(alphabet,max_len):
    if max_len <= 0: return
    for c in alphabet:
        yield c
    for c in alphabet:
        for next in generate(alphabet,max_len-1):
            yield c + next

def md5hash(phrase):
    bytesphrase = str.encode(phrase)
    hashfun = hashlib.md5(bytesphrase)
    hashed_phrase = hashfun.hexdigest()
    return hashed_phrase


if __name__ == "__main__":
   alphabet = string.ascii_lowercase
   password = "password"
   length = len(password)

   #Hashing
   hashpass = md5hash(password)

   start = time.time()
   for com in generate(alphabet,length):
       hashtest = md5hash(com)
       if hashtest == hashpass:
           print("You have successfully cracked the password {} in {} seconds..".format("'"+password+"'",time.time()-start))

