
from AES import AES
from AES_SB import AES_SB
from AES_SR import AES_SR
from AES_MC import AES_MC


master_key = 0x2b7e151628aed2a6abf7158809cf4f3c
master_message = 0x1597C4EF331CC28B7E6D1B2EB3EA3B95

def asHexMatrix(cypher):
    matrix = [[0 for i in range(4)] for j in range(4)]
    chex = hex(cypher)
    for i in range(4):
        for j in range(4):
            index = (i * 4 + j) * 2 + 2
            matrix[j][i] = chex[index:index+2]
    return matrix

def printMatrix(aMatrix):
    for i in range(len(aMatrix)):
        print(aMatrix[i])

def subByteTest_identidad():
    aes = AES_SB(master_key)
    m = 0x1597C4EF331CC28B7E6D1B2EB3EA3B95
    c = aes.encrypt(m)
    for i in range(128):
        for j in range(i+1, 128):
            ci = aes.encrypt(m ^ (1 << i))
            cj = aes.encrypt(m ^ (1 << j))
            ij_mov = 1 << i ^ 1 << j
            cij = aes.encrypt(m ^ ij_mov)
            #print(hex(cij), end="\r", flush=True)
            assert(c == ci ^ cj ^ cij)
            
def subByteTest():
    aes = AES(master_key)
    m = 0x1597C4EF331CC28B7E6D1B2EB3EA3B95
    c = aes.encrypt(m)
    for i in range(128):
        for j in range(i+1, 128):
            ci = aes.encrypt(m ^ (1 << i))
            cj = aes.encrypt(m ^ (1 << j))
            ij_mov = 1 << i ^ 1 << j
            cij = aes.encrypt(m ^ ij_mov)
            #print(hex(cij), end="\r", flush=True)
            assert(c != ci ^ cj ^ cij)

def shiftRowsTest_identidad():
    aes = AES_SR(master_key)
    m = 0x1597C4EF331CC28B7E6D1B2EB3EA3B95
    c = aes.encrypt(m)
    hexC = hex(c)
    for i in range(4):
        mi = m ^ (1 << i * 32)
        ci = aes.encrypt(mi)
        hexCi = hex(ci)
        a = 8 * (3 - i) + 2
        b = a + 8
        print("Columnas diferentes: {}    {} ".format(hexC[a:b],hexCi[a:b]))
        printMatrix(asHexMatrix(c))
        print("")
        printMatrix(asHexMatrix(ci))
        print("")
    

def mixColumnsTest_identidad():
    aes = AES_MC(master_key)
    m = 0x1597C4EF331CC28B7E6D1B2EB3EA3B95
    c = aes.encrypt(m)
    for i in range(4):
        mi = m ^ (1 << i * 32)
        ci = aes.encrypt(mi)
        print("cambiado un byte de la ultima fila")
        printMatrix(asHexMatrix(c))
        print("")
        printMatrix(asHexMatrix(ci))
        print("")


print("Test Sub Byte identidad")
subByteTest_identidad()
print("Test Sub Byte identidad completado")

print("Test Sub Byte")
subByteTest()
print("Test Sub Byte completado")

print("Test Shift Rows identidad")
shiftRowsTest_identidad()
print("Test Shift Rows identidad completado")

print("Test Mix Columns identidad")
mixColumnsTest_identidad()
print("Test Mix Columns identidad completado")
