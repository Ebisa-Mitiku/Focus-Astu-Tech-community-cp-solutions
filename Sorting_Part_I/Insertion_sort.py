#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    e=arr[len(arr)-1]
    f=len(arr)-2
    b=len(arr)-1
    while(f>=0):
        if(arr[f]>e):
            arr[b]=arr[f]
            print(*arr)
            f-=1
            b-=1
        else:
            arr[b]=e
            print(*arr)
            break
    if(f==-1):
        arr[0]=e
        print(*arr)


    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
