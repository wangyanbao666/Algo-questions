#Uses python3

import sys
import queue


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    #write your code here
    distance[s]=0
    reachable[s]=1
    negative=[]
    for i in range(len(adj)+2):
        t = 0
        for u in range(len(adj)):
            edge = adj[u]
            for end in range(len(edge)):
                v = edge[end]
                if distance[v] > distance[u] + cost[u][end]:
                    reachable[v] = 1
                    distance[v] = distance[u] + cost[u][end]
                    if i==len(adj)+1:
                        negative.append(v)
                    t = 1
        if t == 0:
            break

    while len(negative)!=0:
        u=negative.pop(0)
        shortest[u]=0
        for v in adj[u]:
            if shortest[v]==1:
                negative.append(v)


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
    s = data[0]
    s -= 1
    distance = [float('inf')] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

# 5 4 1 2 1 4 1 2 2 3 2 3 1 -5 4
# 6 8 2 3 -1 3 2 -1 1 4 1 1 5 1 1 6 1 2 4 1 2 5 1 2 6 1 1
# 4 5 1 2 100 1 3 100 3 4 -1 4 3 -1 4 2 100 2
# 5 7 1 2 10 2 3 5 1 3 100 3 5 7 5 4 10 4 3 -18 5 1 -1 1
