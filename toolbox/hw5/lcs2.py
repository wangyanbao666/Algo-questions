#Uses python3

import sys
import numpy as np

def lcs2(s, t):
    count=0
    #del:1,ins:2,dismatch:3,match:0
    operation=np.zeros((len(s)+1,len(t)+1))
    for i in range(1,len(s)+1):
        operation[i,0]=1
    for j in range(1,len(t)+1):
        operation[0,j]=2

    matric=np.zeros((len(s)+1,len(t)+1))
    for i in range(len(s)+1):
        matric[i,0]=i
    for j in range(len(t)+1):
        matric[0,j]=j

    for i in range(1,len(s)+1):
        for j in range(1,len(t)+1):
            de=matric[i-1,j]+1
            ins=matric[i,j-1]+1
            mismatch=matric[i-1,j-1]+1
            match=matric[i-1,j-1]
            if s[i-1]==t[j-1]:
                matric[i,j]=min(de,ins,match)
                if matric[i,j]==de:
                    operation[i,j]=1
                elif matric[i,j]==ins:
                    operation[i,j]=2
                else:
                    operation[i,j]=0
                if match == ins and i<=j:
                    operation[i, j] = 2
                if match == de and i>=j:
                    operation[i, j] = 1
            else:
                matric[i,j]=min(de,ins,mismatch)
                if matric[i,j]==mismatch:
                    operation[i,j]=3
                elif matric[i,j]==ins:
                    operation[i,j]=2
                else:
                    operation[i,j]=1
                if mismatch==ins and i<=j:
                    operation[i, j] = 2
                if mismatch==de and i>=j:
                    operation[i,j]=1
    i=len(s)
    j=len(t)
    while i>0 and j>0:
        if operation[i,j]==3:
            i-=1
            j-=1
        elif operation[i,j]==2:
            j-=1
        elif operation[i,j]==1:
            i-=1
        elif operation[i,j]==0:
            i-=1
            j-=1
            count+=1
    # print(operation)
    # print(matric)
    return count


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))

# 4 2 7 8 3 4 5 2 8 7

# 3 2 3 9 4 2 9 7 8