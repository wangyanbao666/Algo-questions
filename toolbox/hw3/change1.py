# Uses python3
import sys

def get_change(m):
    a=m//10
    b=m%10//5
    c=m%5
    return a+b+c

if __name__ == '__main__':
    # m = int(sys.stdin.read())
    m=int(input())
    print(get_change(m))
