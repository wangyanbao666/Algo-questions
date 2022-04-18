#Uses python3

import sys
import numpy as np

def max_dot_product(a, b):
    #write your code here
    a=np.array(a)
    a.sort()
    b=np.array(b)
    b.sort()
    res=np.dot(a,b)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
# 3 1 3 -5 -2 4 1
#1 23 39
