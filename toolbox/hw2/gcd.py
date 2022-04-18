# Uses python3
import sys

def gcd_naive(a, b):

    a,b=max(a,b),min(a,b)
    while b%a!=0:
        b,a = a,b%a

    return a

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))