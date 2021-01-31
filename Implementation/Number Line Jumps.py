#find the exact question here:
#https://www.hackerrank.com/challenges/kangaroo/problem
#or
#https://hackerrank-challenge-pdfs.s3.amazonaws.com/22477-kangaroo-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1612130533&Signature=%2BqQ5rRfmZVirvi6TjdSifjY61uE%3D&response-content-disposition=inline%3B%20filename%3Dkangaroo-English.pdf&response-content-type=application%2Fpdf
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    #getting the first jump
    a=x1+v1
    b=x2+v2
    if(a==b):#in case first jump yields in match
        return("YES")
    elif (v2<v1):#since x1<x2 the only possiblity for the match is when v1 is greater than v2 and hence the kangaroo A would be able to catch the kangaroo B in future
        while a<=b : #considering the positions only when they are equal or less
            a=a+v1 #iterating the jump since we checked the first time , just realised first if can be removed.
            b=b+v2
            if (a == b):#if the location matched on this iteration
                return("YES")
                break
        if (a>b):#just in case while ran completely
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
