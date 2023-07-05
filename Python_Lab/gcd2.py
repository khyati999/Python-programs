def gcd(m,n):
    i=min(m,n)
    
    while i>0:
        if(m%i)==0 and (n%i)==0:
            return(i)
        else:
            i=i-1
m=14
n=63
print(gcd(m,n))