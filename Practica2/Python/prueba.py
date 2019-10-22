def  GF_product_p(a, b):
    expb = 0
    count = 0
    while(b>1):
        count+= 1
        b=b/2
        if (b%2==1):
            expb+=count
    while(expb>0):
        expb-=1
        a=a*2
        if(a>255):
            a-=256
            a=a^29
    print(a)
