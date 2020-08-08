import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    res=0
    maxcount=0

    while n>0:
        if n%2==1:
            res+=1
            if res>maxcount:
                maxcount=res
        
        else:
            res=0
        
        n//=2
    print(maxcount)
