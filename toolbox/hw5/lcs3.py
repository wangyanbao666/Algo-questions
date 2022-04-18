#Uses python3

import sys
import numpy as np

def lcs3(a, b, c):
    #write your code here
    count=0
    operation=np.zeros((len(a)+1,len(b)+1,len(c)+1))
    for i in range(1, len(a) + 1):
        operation[i, 0, 0] = 1
    for j in range(1, len(b) + 1):
        for i in range(len(a) + 1):
            operation[i, j, 0] = 2
    for k in range(1, len(c) + 1):
        for i in range( len(a) + 1):
            operation[i, 0, k] = 3

    matric=np.zeros((len(a)+1,len(b)+1,len(c)+1))
    for i in range(1,len(a)+1):
        matric[i,0,0]=i
    for j in range(1,len(b)+1):
        for i in range(len(a) + 1):
            matric[i,j,0]=j
    for k in range(1,len(c)+1):
        for i in range(len(a) + 1):
            matric[i,0,k]=k

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            for k in range(1,len(c)+1):
                de1 = matric[i - 1, j,k] + 1
                de2 = matric[i, j - 1,k] + 1
                de3=matric[i,j,k-1]+1
                mismatch = matric[i - 1, j - 1,k-1] + 1
                match = matric[i - 1, j - 1,k-1]
                if a[i - 1] == b[j - 1] and a[i-1]==c[k-1] and b[j-1]==c[k-1]:
                    matric[i, j,k] = min(de1, de2,de3, match)
                    if matric[i, j,k] == de1:
                        operation[i, j,k] = 1
                    elif matric[i, j,k] == de2:
                        operation[i, j,k] = 2
                    elif matric[i,j,k]==de3:
                        operation[i,j,k]=3
                    else:
                        operation[i, j,k] = 0
                    if match == de2 and j<=i and j<=k:
                        operation[i, j,k] = 2
                    elif match == de1 and i<=j and i<=k:
                        operation[i, j,k] = 1
                    elif match==de3 and k<=i and k<=j:
                        operation[i,j,k]=3

                else:
                    matric[i, j,k] = min(de1, de2,de3, mismatch)
                    if matric[i, j,k] == mismatch:
                        operation[i, j,k] = 4
                    elif matric[i, j,k] == de2:
                        operation[i, j,k] = 2
                    elif matric[i,j,k]==de1:
                        operation[i, j,k] = 1
                    else:
                        operation[i,j,k]=3
                    if mismatch == de2 and j<=i and j<=k:
                        operation[i, j,k] = 2
                    elif mismatch == de1 and i<=j and i<=k:
                        operation[i, j,k] = 1
                    elif mismatch==de3 and k<=i and k<=j:
                        operation[i,j,k]=3
    i = len(a)
    j = len(b)
    k=len(c)
    while i > 0 and j > 0 and k>0:
        if operation[i, j,k] == 4:
            i -= 1
            j -= 1
            k-=1
        elif operation[i,j,k]==3:
            k-=1
        elif operation[i, j,k] == 2:
            j -= 1
        elif operation[i, j,k] == 1:
            i -= 1
        elif operation[i, j,k] == 0:
            i -= 1
            j -= 1
            k-=1
            count += 1
    print(matric)
    print(operation)
    return count

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))

# 5 8 3 2 1 7 7 8 2 1 3 8 10 7 6 6 8 3 1 4 7
