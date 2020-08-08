import math

class Calculator:
    def power(self,n,p):
        if n<0 or p<0:
            return ValueError("n and p should be non-negative")

        return int(math.pow(n,p))

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)
