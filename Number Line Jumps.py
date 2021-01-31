#find the exact question here:
#https://www.hackerrank.com/challenges/kangaroo/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    a=x1+v1
    b=x2+v2
    if(a==b):
        return("YES")
    elif (v2<v1):
        while a<=b :
            a=a+v1
            b=b+v2
            if (a == b):
                return("YES")
                break
        if (a>b):
            return ("NO")
              
    else:
        return("NO")
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
