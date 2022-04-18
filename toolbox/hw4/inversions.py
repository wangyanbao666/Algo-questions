# Uses python3
import sys

def merge(a,b):
    num=0
    ac=[]
    # print(a,b)
    while len(a)!=0 and len(b)!=0:
        if a[0]<=b[0]:
            ac.append(b[0])
            b.remove(b[0])
        else:
            ac.append(a[0])
            a.remove(a[0])
            num+=len(b)
    ac+=a
    ac+=b
    return ac,num

num=0
def get_number_of_inversions(a):
    if len(a)<=1:
        return a
    else:
        avg=len(a)//2
        l=get_number_of_inversions(a[:avg])
        r=get_number_of_inversions(a[avg:])
        ac,plus=merge(l,r)
        # print(plus)
        global num
        num+=plus
        return ac


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    get_number_of_inversions(a)
    print(num)
# 5 2 3 9 2 9