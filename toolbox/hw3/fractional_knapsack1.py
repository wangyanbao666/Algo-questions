# Uses python3
import sys
import numpy as np

def get_optimal_value(capacity, weights, values):
    value = 0.
    bc=np.array(values)
    c=np.array(weights)
    a=list(bc/c)
    x=np.argsort(a)
    bc=list(bc[x])[::-1]
    c=list(c[x])[::-1]
    for i,j in zip(c,bc):
        if i<=capacity:
            capacity-=i
            value+=j
        else:
            w=capacity
            value+=w*j/i
            break
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    # data = list(map(int, input().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
# 3 50 60 20 100 50 120 30