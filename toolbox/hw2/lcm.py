# Uses python3
import sys

def lcm_naive(a, b):
    mx, mn = max(a, b), min(a, b)
    while mx % mn != 0:
        mx, mn = mn, mx % mn

    return int(a*b/mn)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

