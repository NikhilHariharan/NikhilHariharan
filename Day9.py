import math
import os
import random
import re
import sys

# Complete the factorial function below.
def recur_factorial(n):
    if n==1:
        return (n)
    else:
        return(n*recur_factorial(n-1))

if __name__ == '__main__':

    n = int(input())

    result = recur_factorial(n)

    print(result)
