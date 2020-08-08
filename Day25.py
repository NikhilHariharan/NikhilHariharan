from math import sqrt

T=int(input())

def prime(n):
    if n==1:
        return(False)

    i=2
    while i<=sqrt(n):
        if n%i==0:
            return(False)
        i+=1
    return(True)

for i in range(T):
    num=int(input())
    isPrime=prime(num)
    if isPrime:
        print("Prime")
    else:
        print("Not Prime")
