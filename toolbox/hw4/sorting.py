# Uses python3
import sys
import random

# def partition3(a, l, r):
#     #write your code here
#     pass

def partition3(a, l, r):
    x = a[l]
    j = l
    p=r
    i=l+1
    while i<p:
        if a[i] < x:
            j += 1
            a[i], a[j] = a[j], a[i]
            i+=1
        elif a[i]==x:
            p -= 1
            a[i],a[p]=a[p],a[i]
        else:
            i+=1
    a[l],a[j]=a[j],a[l]
    j+=1
    m=min(p-j,r-p)
    f=r
    for i in range(m):
        a[f-1], a[j] = a[j], a[f-1]
        f-=1
        j+=1
    return j-r+p-1,j


def randomized_quick_sort(a, l, r):
    if l >= r-1:
        return
    k = random.randint(l, r-1)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m,j = partition3(a, l, r)
    randomized_quick_sort(a, l, m);
    randomized_quick_sort(a, j, r);


if __name__ == '__main__':
    # input = sys.stdin.read()
    n, *a = list(map(int, input().split()))
    randomized_quick_sort(a, 0, n)
    for x in a:
        print(x, end=' ')
# 5 2 3 9 2 9
# 22 4 4 -2 -2 -3 -4 -1 3 2 3 -4 0 1 1 -1 -1 3 -1 -4 2 -2 4