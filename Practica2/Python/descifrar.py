from Crypto.Cipher import AES

fkey = open("2019_09_25_17_00_56_hector.baiges.key", "rb")
key = fkey.read()
print("  ")
print("inicio")
print("  ")
print("key: " , key)

f = open("2019_09_25_17_00_56_hector.baiges.enc", "rb")
fopen = f.read()
iv = fopen[:AES.block_size]
text = fopen[AES.block_size:]

print("iv: " , iv)

f2 = open("2019_09_25_17_00_56_hector_baiges.dec", "wb+")
obj = AES.new(key, AES.MODE_OFB,iv)
des = obj.decrypt(text)
f2.write(des)
print(des)