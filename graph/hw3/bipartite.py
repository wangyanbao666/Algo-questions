#Uses python3

import sys
import queue


def bipartite(adj):
    #write your code here
    color=[0]*len(adj)
    c=1
    for i in range(len(adj)):
        if color[i]==0:
            q=[i]
            while len(q)!=0:
                c = c % 2 + 1
                newq = []
                for v in q:
                        color[v]=c
                        for j in adj[v]:
                            if color[j]==0 and j not in q:
                                newq.append(j)
                            else:
                                if color[j]==c:
                                    return 0
                q=newq
    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    # input=input()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    # print(adj)
    print(bipartite(adj))


# 5 4 5 2 4 2 3 4 1 4
# 4 4 1 2 4 1 2 3 3 1