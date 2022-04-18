# Uses python3
import sys
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

def fast_count_segments(starts, ends, points):
    li=[]
    l=0
    r=0
    cnt=len(points)*[0]
    for i in starts:
        li.append((i,'l'))
    for i in ends:
        li.append((i,'r'))
    for i in points:
        li.append((i[0],'p',i[1]))
    # print(li)
    randomized_quick_sort(li,0,len(li))
    # print(li)
    for i in range(len(li)-1):
        if li[i][0]==li[i+1][0]:
            if li[i][1]=='p' and li[i+1][1]=='l':
                li[i],li[i+1]=li[i+1],li[i]
            elif li[i][1] == 'r' and li[i + 1][1] == 'p':
                li[i], li[i + 1] = li[i + 1], li[i]
    for i in li:
        if i[1]=='p':
            s=l-r
            cnt[i[2]]=s
        elif i[1]=='l':
            l+=1
        else:
            r+=1

    return cnt

# def naive_count_segments(starts, ends, points):
#     cnt = [0] * len(points)
#     for i in range(len(points)):
#         for j in range(len(starts)):
#             if starts[j] <= points[i] <= ends[j]:
#                 cnt[i] += 1
#     return cnt

if __name__ == '__main__':
    # input = sys.stdin.read()
    data = list(map(int, input().split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    for i in range(len(points)):
        points[i]=(points[i],i)
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')

# 2 3 0 5 7 10 1 6 11

# 3 2 0 5 -3 2 7 10 1 6

# 1 3 -10 10 -100 100 0

