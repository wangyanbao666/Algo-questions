#Uses python3
import sys
import math

def minimum_distance(x, y):
    result = 0.
    #write your code here
    cost=[float('inf')]*len(range(len(x)))
    cost[0] = 0
    PrioQ=list(range(len(x)))
    # print(PrioQ)
    # for i in range(len(x)):
    #     PrioQ[i]=cost[i]
    for i in range(len(x)):
        v=cost.index(min(cost))
        result+=cost[v]
        cost[v]=float('inf')
        PrioQ[v]=-1
        for z in range(len(cost)):
            if z!=v:
                if PrioQ[z]!=-1:
                    w=math.sqrt((x[v]-x[z])**2+(y[v]-y[z])**2)
                    if cost[z]>w:
                        cost[z]=w
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    # input=input()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))


# 4 0 0 0 1 1 0 1 1
# 5 0 0 0 2 1 1 3 0 3 2
    var = {1, 2, 3}
