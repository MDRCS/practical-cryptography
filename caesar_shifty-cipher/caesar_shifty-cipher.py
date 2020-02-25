

def caesar_encoding(message,shift=2):
    cipher = ""
    for ch in message:
        if ord(ch)>=65 and ord(ch)<=90 or ord(ch)>=97 and ord(ch) <= 122:
            if ord(ch) >= 65 and ord(ch) <= 90:
                if ord(ch) + shift > 90:
                    asci = (ord(ch) + shift) - 90
                    asci = asci + 65
                    cipher += chr(asci)
                else:
                    asci = ord(ch) + shift
                    cipher += chr(asci)

            elif ord(ch)>=97 and ord(ch)<= 122:
                if ord(ch) + shift > 122:
                    asci = (ord(ch) + shift) - 122
                    asci = asci + 97
                    cipher += chr(asci)
                else:
                    asci = ord(ch) + shift
                    cipher += chr(asci)
        else:
            cipher += ch
    return cipher


def caesar_decoding(cipher,shift=2):
    cleartext = ""
    for c in cipher:
        if ord(c) >= 65 and ord(c) <= 90 or ord(c) >= 97 and ord(c) <= 122:
            if ord(c) >= 65 and ord(c) <= 90:
                if ord(c) - shift < 65:
                    asci = 65 - (ord(c) - shift)
                    asci = 90 - asci
                    cleartext += chr(asci)
                else:
                    asci = ord(c) - shift
                    cleartext += chr(asci)
            elif ord(c) >= 97 and ord(c) <= 122:
                if ord(c) - shift < 97:
                    asci = 97 - (ord(c) - shift)
                    asci = 122 - asci
                    cleartext += chr(asci)
                else:
                    asci = ord(c) - shift
                    cleartext += chr(asci)
        else:
            cleartext += c

    return cleartext


if __name__ == "__main__":
    cipher = caesar_encoding("Hello World",3)
    print(cipher)

    cleartext = caesar_decoding(cipher,3)
    print(cleartext)
