#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    LR=0
    RL=0
    j_jump = int(len(arr))-1
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if i == j:
                LR+=int(arr[i][j])
            if j==j_jump:
                j_jump-=1
                RL+=int(arr[i][j])
        
    return abs(LR-RL)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
