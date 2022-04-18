# Uses python3
import sys
import itertools
import numpy as np

def partition3(A):
    for c in itertools.product(range(3), repeat=len(A)):
        # print(c)
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1
        # print(sums)

    return 0

def partition3_new(A):
    total=sum(A)
    if total%3!=0:
        return 0
    else:
        stantard=int(total/3)
        matric=np.zeros((len(A)+1,stantard+1))
        for i in range(len(A)+1):
            for j in range(stantard+1):
                matric[i, j] = matric[i - 1, j]
                if A[i - 1] <= j:
                    val = matric[i - 1, j - A[i - 1]] + A[i - 1]
                    if matric[i, j] < val:
                        matric[i, j] = val
        if val!=stantard:
            return 0
        else:
            i=len(A)
            A_copy=A
            j=stantard
            obj=matric[i,j]
            while obj!=0:
                if matric[i,j]!=matric[i-1,j]:
                    i-=1
                else:
                    A.pop(i)
                    j-=A_copy[i]
                    i -= 1
                obj = matric[i, j]
        #the second round
        matric = np.zeros((len(A) + 1, stantard + 1))
        for i in range(len(A) + 1):
            for j in range(stantard + 1):
                matric[i, j] = matric[i - 1, j]
                if A[i - 1] <= j:
                    val = matric[i - 1, j - A[i - 1]] + A[i - 1]
                    if matric[i, j] < val:
                        matric[i, j] = val
        if val != stantard:
            return 0
    return 1


if __name__ == '__main__':
    # input = sys.stdin.read()
    n, *A = list(map(int, input().split()))
    print(partition3(A))

# 11 17 59 34 57 17 23 67 1 18 2 59
# 13 1 2 3 4 5 5 7 7 8 10 12 19 25
