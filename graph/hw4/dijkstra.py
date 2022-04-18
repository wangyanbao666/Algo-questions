#Uses python3

import sys
import queue


def distance(adj, cost, s, t):
    dist=[float('inf')]*len(adj)
    dist[s]=0
    q= {}
    for i in range(len(adj)):
        q[i]=dist[i]
    while len(q)!=0:
        # print(q)
        m=min(q.values())
        index=list(q.values()).index(m)
        u=list(q.keys())[index]
        del q[u]
        # for i in q.keys():
        #     q[i] = dist[i]
        for v in range(len(adj[u])):
            if dist[adj[u][v]]>dist[u]+cost[u][v]:
                # print(dist[u],cost[u][v])
                dist[adj[u][v]]=dist[u]+cost[u][v]
        for i in q:
            q[i] = dist[i]
    if dist[t]==float('inf'):
        return -1
    return dist[t]


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
    s, t = data[0] - 1, data[1] - 1
    # print(adj)
    print(distance(adj, cost, s, t))


# 4 4 1 2 1 4 1 2 2 3 2 1 3 5 1 3
# 5 9 1 2 4 1 3 2 2 3 2 3 2 1 2 4 2 3 5 4 5 4 1 2 5 3 3 4 4 1 5