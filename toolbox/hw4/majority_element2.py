# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)
    mid=(left+right)//2
    if len(a)==0:
        return -1
    else:
        if x==a[mid]:
            return mid
        if len(a)==1:
            return -1
        else:
            if x>a[mid]:
                return binary_search(a[mid+1:],x)
            elif x<a[mid]:
                return binary_search(a[:mid],x)

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    return -1


if __name__ == '__main__':
    # input = sys.stdin.read()
    n, *a = list(map(int, input().split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)



#5 2 3 9 2 2