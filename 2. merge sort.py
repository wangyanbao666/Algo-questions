import sys
sys.setrecursionlimit(1000)

a=[1,23,21,45,46,23,7,9]

def merge_sort(a,p,r):
    if p<r:
        q=(p+r)//2
        merge_sort(a,p,q)
        merge_sort(a,q,r)
        merge(a,p,q,r)
    else:
        return a

def merge(a,p,q,r):
    L = []
    R = []
    n1=q-p
    n2=r-q+1
    for i in range(0,n1):
        L.append(a[p+i])
    for j in range(0,n2):
        R.append(a[q+j])
    # L.append(100000)
    # R.append(100000)
    i=0
    j=0
    for n in range(p,r):
        if L[i]>R[j]:
            a[n]=R[j]
            j+=1
        else:
            a[n]=L[i]
            i+=1

merge_sort(a,0,8)
print(a)











