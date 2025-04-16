import math
import random
import re
import sys

if __name__ == '__main__':

    nm = input().split()

n = int(nm[0])

m = int(nm[1])

arr = []

for i in range(n):

    arr.append(list(map(int, input().rstrip().split())))

k = int(input())

answer=sorted(arr, key=lambda x:x[k])
print(answer)