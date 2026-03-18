#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    c=0
    for i in range(len(a)-1):
        f=False
        for j in range(len(a)-(i+1)):
            if(a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
                f=True
                c=c+1
        if(not f):
            break
    print("Array is sorted in "+ str(c)+ " swaps.")
    print("First Element: "+str(a[0]))
    print("Last Element: "+ str(a[len(a)-1]))
    
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
