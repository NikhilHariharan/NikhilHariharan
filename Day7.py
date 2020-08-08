#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())
    arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

rarr = map(str, arr[::-1])
print(" ".join(rarr))
