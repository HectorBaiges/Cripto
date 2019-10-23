import time
import GF256 as gf


def timeForGF_product_T(a, b):
    start = time.perf_counter()
    gf.GF_product_t(a, b)
    end = time.perf_counter()
    return end - start

def timeForGF_product_P(a, b):
    start = time.perf_counter() 
    gf.GF_product_p(a, b)
    end = time.perf_counter() 
    return end - start

def GF_product_TvsGF_productP(b):
    results = [[0.0, 0.0] for y in range(256)]
    for i in range(1,256):
        meanT = 0
        for _ in range(10):
            meanT += timeForGF_product_T(i, b)
        meanT = meanT / 10

        meanP = 0
        for _ in range(10):
            meanP += timeForGF_product_P(i, b)
        meanP = meanP / 10

        results[i][0] = meanT
        results[i][1] = meanP
    return results


if __name__ == "__main__":
    #results02 = GF_product_TvsGF_productP(10, 0x02)
    #results03 = GF_product_TvsGF_productP(10, 0x03)
    #results09 = GF_product_TvsGF_productP(10, 0x09)
    #results0B = GF_product_TvsGF_productP(10, 0x0B)
    #results0D = GF_product_TvsGF_productP(10, 0x0D)
    gf.GF_Tables()
    results0E = GF_product_TvsGF_productP(0x02)
    print(results0E)
