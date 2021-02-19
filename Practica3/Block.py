#!/usr/bin/env python
import random
import hashlib
#from Crypto.Util import number
#import numpy 

class rsa_key:
    def __init__(self,bits_modulo=2048,e=2**16+1):
        '''
        genera una clau RSA (de 2048 bits i amb exponent públic 2**16+1 per defecte)
        '''
        self.publicExponent = e
        self.primeP = self.generateRandomPrime(int(bits_modulo/2),0)
        self.primeQ = self.generateRandomPrime(int(bits_modulo/2),self.primeP)
        self.modulus = self.primeP * self.primeQ
        phiN = (self.primeP - 1) * (self.primeQ - 1)
        self.privateExponent = self.modinv(self.publicExponent, (self.primeP - 1) * (self.primeQ - 1)) #self.privateExponent = self.modinv(self.publicExponent, phiN)
        self.privateExponentModulusPhiP = self.privateExponent % (self.primeP - 1)
        self.privateExponentModulusPhiQ = self.privateExponent % (self.primeQ - 1)
        self.inverseQModulusP = self.modinv(self.primeQ,self.primeP)
        
    def egcd(self,a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    def modinv(self,a, m):
        g, x, y = self.egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m
        return 1
    
    def is_Prime_Miller(self,n):
        """
        Miller-Rabin primality test.
    
        A return value of False means n is certainly not prime. A return value of
        True means n is very likely a prime.
        """
        if n!=int(n):
            return False
        n=int(n)
        #Miller-Rabin test for prime
        if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
            return False
    
        if n==2 or n==3 or n==5 or n==7:
            return True
        s = 0
        d = n-1
        while d%2==0:
            d>>=1
            s+=1
        assert(2**s * d == n-1)
    
        def trial_composite(a):
            if pow(a, d, n) == 1:
                return False
            for i in range(s):
                if pow(a, 2**i * d, n) == n-1:
                    return False
            return True  
    
        for i in range(5):#number of trials 
            a = random.randrange(2, n)
            if trial_composite(a):
                return False
        return True 
    
    def generateRandomPrime(self,bits,previous):
        #return number.getPrime(1024)
        n = random.getrandbits(bits)
        n = n+(1-n%2)
        while(n!=previous and not self.is_Prime_Miller(n)):
            n +=2
        return n
        
    def sign(self,message):
        '''
        retorma un enter que és la signatura de "message" feta amb la clau RSA fent servir el TXR
        '''
        
        h = int(hashlib.sha256(str(message).encode('utf-8')).hexdigest(),16)
        
        d1 = self.privateExponentModulusPhiP 
        d2 = self.privateExponentModulusPhiQ
        c1 = pow(h, d1, self.primeP)
        c2 = pow(h, d2, self.primeQ)
        q1 = self.inverseQModulusP
        
        qq1 = self.primeQ*q1
        pp1 = 1 - qq1
    
        return (c1*qq1+c2*pp1) % self.modulus
    
    def sign_slow(self,message):
        '''
        retorma un enter que és la signatura de "message" feta amb la clau RSA sense fer servir el TXR
        '''
        h = int(hashlib.sha256(str(message).encode('utf-8')).hexdigest(),16)
        r = pow(h,self.privateExponent, self.modulus)
        return r
    
class rsa_public_key:
    def __init__(self, rsa_key):
        '''
        genera la clau pública RSA asociada a la clau RSA "rsa_key"
        '''
        self.publicExponent = rsa_key.publicExponent
        self.modulus = rsa_key.modulus

    def verify(self, message, signature):
        '''
        retorna el booleà True si "signature" es correspon amb una
        signatura de "message" feta amb la clau RSA associada a la clau
        pública RSA.
        En qualsevol altre cas retorma el booleà False
        '''
        h = int(hashlib.sha256(str(message).encode('utf-8')).hexdigest(),16)
        firm = pow(signature, self.publicExponent, self.modulus)
        return h == firm
        
        
class transaction:
    def __init__(self, message, RSAkey):
        '''
        genera una transacció signant "message" (entero, no hace falta hacer el hash)amb la clau "RSAkey"
        '''
        self.public_key = rsa_public_key(RSAkey)
        self.message = message
        self.signature = RSAkey.sign(self.message)
        
    def verify(self):
        '''
        retorna el booleà True si "signature" es correspon amb una
        signatura de "message" feta amb la clau pública "public_key".
        En qualsevol altre cas retorma el booleà False
        '''
        return self.public_key.verify(self.message, self.signature)
    
    
class block:
    def __init__(self):
        '''
        crea un bloc (no necesàriamnet vàlid)
        '''
        self.block_hash = 2**255
        self.previous_block_hash = 0
        self.transaction = None
        self.seed = 0
        
    def genesis(self,transaction):
        '''
        genera el primer bloc d’una cadena amb la transacció "transaction" que es caracteritza per:
        - previous_block_hash=0
        - ser vàlid
        '''
        self.previous_block_hash = 0
        self.transaction = transaction
        
        while(self.block_hash > 2**240):
            
            self.seed = random.getrandbits(1024)
            entrada=str(self.previous_block_hash)
            entrada=entrada+str(transaction.public_key.publicExponent)
            entrada=entrada+str(transaction.public_key.modulus)
            entrada=entrada+str(transaction.message)
            entrada=entrada+str(transaction.signature)
            entrada=entrada+str(self.seed)
            h=int(hashlib.sha256(entrada.encode()).hexdigest(),16)
            self.block_hash = h
        
    def next_block(self, transaction):
        '''
        genera el següent block vàlid amb la transacció "transaction"

        '''
        self.previous_block_hash = self.block_hash
        self.transaction = transaction
        
        while(self.block_hash > 2**240):
            
            self.seed = random.getrandbits(1024)
            entrada=str(self.previous_block_hash)
            entrada=entrada+str(transaction.public_key.publicExponent)
            entrada=entrada+str(transaction.public_key.modulus)
            entrada=entrada+str(transaction.message)
            entrada=entrada+str(transaction.signature)
            entrada=entrada+str(self.seed)
            h=int(hashlib.sha256(entrada.encode()).hexdigest(),16)
            self.block_hash = h

    
    def verify_block(self):
        '''
        Verifica si un bloc és vàlid:
        -Comprova que el hash del bloc anterior cumpleix las condicions exigides
        -Comprova la transacció del bloc és vàlida
        -Comprova que el hash del bloc cumpleix las condicions exigides
        Si totes les comprovacions són correctes retorna el booleà True.
        En qualsevol altre cas retorma el booleà False
        '''
        
        if (self.previous_block_hash > 2**240): return False
        if (not self.transaction.verify()): return False
        if (self.block_hash > 2**240): return False
        return True
    
    
class block_chain:
    def __init__(self,transaction):
        '''
        genera una cadena de blocs que és una llista de blocs,
        el primer bloc és un bloc "genesis" generat amb la transacció "transaction"
        '''
        self.list_of_blocks = generar_lista(transaction)
        
    def generar_lista(self,transaction):
        '''
        genera llista de blocs
        '''
        blockinicial = block()
        blockinicial.genesis(transaccion)
        lista = []
        lista[0] = block
        return lista
        
    def add_block(self,transaction):
        '''
        afegeix a la llista de blocs un nou bloc vàlid generat amb la transacció "transaction"
        '''
        bloque = block()
        bloque.genesis(transaccion)
        self.list_of_blocks.append(bloque)

    def verify(self):
        '''
        verifica si la cadena de blocs és vàlida:
        - Comprova que tots el blocs són vàlids
        - Comprova que el primer bloc és un bloc "genesis"
        - Comprova que per cada bloc de la cadena el següent és el correcte
        Si totes les comprovacions són correctes retorna el booleà True.
        En qualsevol altre cas retorma el booleà False i fins a quin bloc la cadena és válida
        '''
        i = 0

        if(self.list_of_blocks[0].previous_block_hash != 0): return False, 0 # Comprova que el primer bloc és un bloc "genesis"

        for i in range(1,len(self.list_of_blocks)):
            if(not self.list_of_blocks[0]): return False, i # Comprova que tots el blocs són vàlids

            if(self.list_of_blocks[i-1].block_hash != self.list_of_blocks[i].previous_block_hash): return False, i # Comprova que per cada bloc de la cadena el següent és el correcte
        return True, i

        
        


mensaje = 123456
print("rsa")
rsaClave = rsa_key()
print("rsa_pub")
rsaPublica = rsa_public_key(rsaClave)
print("transaccion")
transaccion = transaction(123456,rsaClave)
print("bloque")
bloque = block()
print("genesis")
bloque.genesis(transaccion)

print(bloque.block_hash)




'''
self.publicExponent = e
self.primeP = self.generateRandomPrime(int(bits_modulo/2),0)
self.primeQ = self.generateRandomPrime(int(bits_modulo/2),self.primeP)
self.modulus = self.primeP * self.primeQ
phiN = (self.primeP - 1) * (self.primeQ - 1)
self.privateExponent = self.modinv(self.publicExponent, (self.primeP - 1) * (self.primeQ - 1)) #self.privateExponent = self.modinv(self.publicExponent, phiN)
self.privateExponentModulusPhiP = self.privateExponent % (self.primeP - 1)
self.privateExponentModulusPhiQ = self.privateExponent % (self.primeQ - 1)
self.inverseQModulusP = self.modinv(self.primeQ,self.primeP)
'''
