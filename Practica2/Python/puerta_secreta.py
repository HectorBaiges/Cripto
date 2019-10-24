from Crypto.Cipher import AES
import os
import hashlib

f = open("2019_09_25_17_00_56_hector.baiges.puerta_trasera.enc", "rb")
text = f.read()

cont = 1
for i in range(128):
  bi = str(bytes ([i]))
  for j in range(128):
    print (cont)
    bj = str(bytes([j]))
    preMasterKey = bi+bi+bi+bi+bi+bi+bi+bi+bj+bj+bj+bj+bj+bj+bj+bj
    print(preMasterKey)
    H = hashlib.sha256(preMasterKey.encode('utf8')).digest()
    K = H[:16]
    VI = H[16:]

    f2 = open("aux.dec", "wb+")
    obj = AES.new(K, AES.MODE_CBC,VI)
    des = obj.decrypt(text)
    f2.write(des)
    typ = os.popen('file aux.dec').read()
    cont = cont+1
    print(typ)
    if "MP4" in typ or "MP3" in typ or "JPG" in typ or "PNG" in typ: 
      f3 = open("result2ElectricBoogaloo.dec","wb+")
      f3.write(des)
      print("HOOOOLA")
