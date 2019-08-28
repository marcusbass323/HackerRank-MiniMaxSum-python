
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):

#Pull max & min index and save to value
    maxVal = max(arr)
    minVal = min(arr)
#Remove/add min and max values from arrays
    arr.remove(maxVal)
    arr1 = sum(arr)
    arr.remove(minVal)
    arr.append(maxVal)
#function to sum Array
    arr2 = sum(arr)
    print(arr1, arr2)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
