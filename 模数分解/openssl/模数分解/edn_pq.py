import random  
  
def gcd(a, b):  
   if a < b:  
     a, b = b, a  
   while b != 0:  
     temp = a % b  
     a = b  
     b = temp  
   return a  
  
def getpq(n,e,d):  
    p = 1  
    q = 1  
    while p==1 and q==1:  
        k = d * e - 1  
        g = random.randint ( 0 , n )  
        while p==1 and q==1 and k % 2 == 0:  
            k /= 2  
            y = pow(g,k,n)  
            if y!=1 and gcd(y-1,n)>1:  
                p = gcd(y-1,n)  
                q = n/p  
    return p,q  
  
def main():  
 
    n = 0xa66791dc6988168de7ab77419bb7fb0c001c62710270075142942e19a8d8c51d053b3e3782a1de5dc5af4ebe99468170114a1dfe67cdc9a9af55d655620bbab  
    e =  0x10001
    d =  0x123c5b61ba36edb1d3679904199a89ea80c09b9122e1400c09adcf7784676d01d23356a7d44d6bd8bd50e94bfc723fa87d8862b75177691c11d757692df8881
    p,q = getpq(n,e,d)  
    print "p: "+hex(p)
    print "q: "+hex(q)  
  
if __name__ == '__main__':  
    main()
