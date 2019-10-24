import time
import GF256 as gf
import numpy as np
import matplotlib.pyplot as plt

def timeForGF_product_T(a, b):
    start = time.process_time()
    gf.GF_product_t(a, b)
    end = time.process_time()
    return end - start

def timeForGF_product_P(a, b):
    start = time.process_time()
    gf.GF_product_p(a, b)
    end = time.process_time()
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

def graphResutlsAsBarChart(results, value):
    n_groups = 256
    
    medians_table = [results[i][0] for i in range(256)]
        
    mediants_poly = [results[i][1] for i in range(256)]
    
    fig, ax = plt.subplots()
        index = np.arange(n_groups)
    bar_width = 0.75
    opacity = 1
    rects1 = plt.bar(index, medians_table, bar_width,
                     alpha=opacity,
                     color='b',
                     label='Product using tables')
    
    rects2 = plt.bar(index + bar_width, mediants_poly, bar_width,
                     alpha=opacity,
                     color='r',
                     label='Product of polynomials')
    plt.xlabel('GF(256)')
    plt.ylabel('Time (s)')
    plt.title('Time comparison multiplying all elements in GF(256) by {}'.format(hex(value)))
    plt.xticks(index + bar_width / 2, ())
    plt.legend()
    
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    #results02 = GF_product_TvsGF_productP(0x02)
    #results03 = GF_product_TvsGF_productP(0x03)
    #results09 = GF_product_TvsGF_productP(0x09)
    #results0B = GF_product_TvsGF_productP(0x0B)
    #results0D = GF_product_TvsGF_productP(0x0D)
    #results0E = GF_product_TvsGF_productP(0x0E)
    gf.GF_Tables()
    prova = 0x0E
    results = GF_product_TvsGF_productP(prova)
    graphResutlsAsBarChart(results, prova)
