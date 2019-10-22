from Crypto.Cipher import AES

obj = AES.new(b'\xb9\x96\xe5\xba\xd3}\x04\x13\xa9\x0f\x05\xa2i\xae\x89\x81', AES.MODE_ECB)
message = "The answer is no"
ciphertext = obj.encrypt(message)
print(ciphertext)
obj2 = AES.new(b'\xb9\x96\xe5\xba\xd3}\x04\x13\xa9\x0f\x05\xa2i\xae\x89\x81', AES.MODE_ECB)
des = obj2.decrypt(ciphertext)
print(des)
