from symmetric_encryption.aes_ecb import aesEncryptor

"""The reason we’re not encrypting the first 54 bytes is because this program is going to
encrypt the contents of a bit map file (BMP) and the header is 54 bytes in length.7 """

if __name__ == "__main__":
	with open("secret.bmp","rb") as reader:
		with open("encrypted_image.bmp","wb+") as writer:
			image_data = reader.read()
			header,body = image_data[:54],image_data[54:]
			body += b"\x00" * (16 - (len(body) % 16))
			writer.write(header+aesEncryptor.update(body))


