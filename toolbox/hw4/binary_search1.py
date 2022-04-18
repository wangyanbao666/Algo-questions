# Uses python3
import sys

def binary_search(a, x,l,r):
    mid=(l+r)//2
    if l==r:
        return -1
    else:
        if x==a[mid]:
            return mid
        if len(a)==1:
            return -1
        else:
            if x>a[mid]:
                return binary_search(a,x,mid+1,r)
            elif x<a[mid]:
                return binary_search(a,x,l,mid)


# def linear_search(a, x):
#     for i in range(len(a)):
#         index=binary_search(a,x)
#     return index

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x,0,len(a)), end = ' ')
# 5 1 5 8 12 13 5 8 1 23 1 11