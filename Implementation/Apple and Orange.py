#find the exact question here:
#https://www.hackerrank.com/challenges/apple-and-orange/problem
#or
#https://hackerrank-challenge-pdfs.s3.amazonaws.com/25220-apple-and-orange-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1612131969&Signature=T8WDHlrQHT0QiBV%2FDicNDHvwOK0%3D&response-content-disposition=inline%3B%20filename%3Dapple-and-orange-English.pdf&response-content-type=application%2Fpdf
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple=0
    orange=0
    for ap in apples:#for iterating through each apple
        if ap+a in range(s,t+1):#getting exact loc of apple and checking if it falls in desired range
            apple=apple+1
    for ora in oranges:
        if ora+b in range(s,t+1):#getting exact loc of orange and checking if it falls in desired range
            orange=orange+1
    print(apple)
    print(orange)
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

    countApplesAndOranges(s, t, a, b, apples, oranges)
