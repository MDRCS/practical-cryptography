import hashlib

""" MD5 IS A HASHFUNCTION THAT IS WEAK TO CRACK SO DON'T USE IT IN A REAK APPLICATION """

#hashing function won't work if you don't give it bytes,
#so there is two solution first open file with rb (read binary)
#status or read it as string and convert it to bytes

if __name__ == "__main__":
    doc = ""
    with open("data.txt","r+") as file:
        for line in file.readlines():
            doc += line

        docbytes = str.encode(doc)
        dochash = hashlib.md5(docbytes)
        print("The hashing of data.txt document is "+dochash.hexdigest())

