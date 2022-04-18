#Uses python3

import sys


def negative_cycle(adj, cost):
    dist=[1000000000]*len(adj)
    dist[0]=0
    # edges=[]
    # for edge in adj:
    #     edges.extend(edge)
    for i in range(len(adj)):
        t=0
        for u in range(len(adj)):
            edge=adj[u]
            for end in range(len(edge)):
                v=edge[end]
                if dist[v]>dist[u]+cost[u][end]:
                    dist[v]=dist[u]+cost[u][end]
                    t=1
        if t==0:
            return 0
    return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    # input=input()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))

# 4 4 1 2 -5 4 1 2 2 3 2 3 1 1