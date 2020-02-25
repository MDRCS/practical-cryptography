import os

def func_xor(msg,msgr):
    list = []
    for b,br in zip(msg,msgr):
        list.append(b^br)

    return bytes(list)


def invert_xor(rs,msg):
    result = []
    for bl,b in zip(rs,msg):
        result.append(bl^b)

    return bytes(result)


if __name__ == "__main__":
    message = b"Hello world" #this is a utf-8 format of binary -> b'Hello world'
    rand_msg = os.urandom(16)

    rs = func_xor(message,rand_msg)
    print(rs)
    cleartext = invert_xor(rs,rand_msg)
    print(cleartext)


