# Uses python3
import sys

def get_change(m):
    #write your code here
    li=(m+1)*[0]
    for i in range(1,m+1):
        li[i]=10000000000
        for j in [1,3,4]:
            if i>=j:
                minnum=li[i-j]+1
                if minnum<li[i]:
                    li[i]=minnum
    return li[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

