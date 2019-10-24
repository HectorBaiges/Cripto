from Crypto.Cipher import AES
import os
import hashlib

f = open("2019_09_25_17_00_56_hector.baiges.puerta_trasera.enc", "rb")
text = f.read()
possible_keys = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
cont = 1
for i in range(62):
  for j in range(62):
    print (cont)
    preMasterKey = possible_keys[i]+possible_keys[i]+possible_keys[i]+possible_keys[i]+possible_keys[i]+possible_keys[i]+possible_keys[i]+possible_keys[i]+possible_keys[j]+possible_keys[j]+possible_keys[j]+possible_keys[j]+possible_keys[j]+possible_keys[j]+possible_keys[j]+possible_keys[j]
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
