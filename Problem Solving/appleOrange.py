#Manuel Ortiz Hernández at 2020
#Problem Solving. Extracted from: https://www.hackerrank.com/challenges/apple-and-orange/problem

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def count_apple_and_oranges(s, t, a, b, apples, oranges):
    apple_counter = 0
    orange_counter = 0

    if not apples and not oranges:
        print(0,0,sep="\n")
        return

    apple_counter = get_distances(apples, a, s, t)
    orange_counter = get_distances(oranges, b, s, t)

    print(apple_counter,orange_counter, sep="\n")
    

def get_distances(fruits, pos, s, t):

    i = 0
    to_add = 0
    while i < len(fruits):
        fruits[i] = pos + fruits[i]

        if fruits[i] >= s and fruits[i] <= t:
            to_add +=1

        i+=1

    return to_add 
    


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    count_apple_and_oranges(s, t, a, b, apples, oranges)
