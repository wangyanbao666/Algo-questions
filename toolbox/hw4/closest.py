#Uses python3
import sys
import math
import random


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

def sort(x,y):
    #write your code here
    li=[]
    for i,j in zip(x,y):
        li.append((i,j))
    randomized_quick_sort(li,0,len(li))
    return li


def minimum_distance(li):
    # print(li)
    if len(li)==1:
        return 1e18
    if len(li)==2:
        return math.sqrt((li[0][0]-li[1][0])**2+(li[0][1]-li[1][1])**2)
    m1=len(li)//2
    m2=m1+1
    mm1=li[m1][0]
    mm2=li[m2][0]
    m=(mm1+mm2)/2
    d1=minimum_distance(li[0:m2])
    d2=minimum_distance(li[m2:])
    # print(d1,d2)
    d=min(d1,d2)

    ml=m-d
    # print(ml)
    l=m1
    rl=m+d
    # print(rl)
    r=m1
    while l>=0 and li[l][0]>ml:
        l-=1
    while r<len(li) and li[r][0]<rl:
        r+=1
    l+=1
    mid=li[l:r]
    # print(mid)
    d_p=d
    for i in range(len(mid)):
        for j in range(i+1,len(mid)):
            x=math.sqrt((mid[i][0] - mid[j][0]) ** 2 + (mid[i][1] - mid[j][1]) ** 2)
            if x<d_p:
                d_p=x
    return d_p

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    li = sort(x, y)
    print("{0:.9f}".format(minimum_distance(li)))

# 4 7 7 1 100 4 8 7 7
# 2 0 0 3 4
# 11 4 4 -2 -2 -3 -4 -1 3 2 3 -4 0 1 1 -1 -1 3 -1 -4 2 -2 4
#11 4 -2 -3 -1 2 -4 1 -1 3 -4 -2
