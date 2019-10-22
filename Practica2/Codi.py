exp = []
log = []
g = 0x02

def GF_product_p(a,b):
    result = 0
    for i in range(8):
        if ((b%2) == 0x01):
            result = result ^a
        aux = a << 1
        if ((aux & 0x100) == 0x100):
            aux ^= 0x1d
        a = aux & 0xFF
        b = b>>1
        
    return result & 0xff

def GF_es_generador(a):
    check = [False] * 256
    check[0] = True
    check[a] = True
    k = 1
    tmp = a
    while (tmp != 1):
        tmp = GF_product_p(tmp, a)
        check[tmp] = True
        k = k + 1
    return (k==255)

def GF_Tables():
    global exp
    global log
    exp = [0x01]
    log = [0] * 256
    for i in range(2**8 -2):
        ant = exp[i]
        prod = GF_product_p(ant,g)
        exp += [prod]
        log[prod] = i+1

def GF_product_T(a,b):
    global exp
    global log
    ret = exp[(log[a] + log[b]) % 255]
    return ret & 0xFF

def GF_invers(a):
    global exp
    global log
    ret = 0
    if a != 0:
        exp = log[a]
        invExp = (0xFF - exp) % 255
        ret = exp[invExp]
    return ret

GF_Tables()
print(GF_product_p(0xff,0x02))
print(GF_product_T(0xff,0x02))
print(exp)
print(log)

