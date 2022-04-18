#Uses python3

import sys

num=1
sign=0

def explore(index,adj,visited,start,end):
    global num,sign
    start[index] = num
    for i in adj[index]:
        if visited[i]==0:
            visited[i] = 1
            end[i] = num
            if end[i]==start[i] and end[i]!=0:
                sign=1
                break
            explore(i,adj,visited,start,end)


def acyclic(adj):
    global num
    visited=[0]*len(adj)
    start=[0]*len(adj)
    end=[0]*len(adj)
    for i in range(len(adj)):
        if visited[i]==0:
            explore(i,adj,visited,start,end)
            num += 1
    return sign

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
    # print(adj)
    print(acyclic(adj))

# 4 4 1 2 4 1 2 3 3 1
# 5 7 1 2 2 3 1 3 3 4 1 4 2 5 3 5
