#Uses python3

import sys

def explore(adj,ls,ccnum,visited,num):
    for i in ls:
        if visited[i]==0:
            ccnum[i]=num
            visited[i]=1
            explore(adj,adj[i],ccnum,visited,num)

def reach(adj):
    CCnum=[0]*len(adj)
    visited=[0]*len(adj)
    num=1
    for i in range(len(adj)):
        if CCnum[i]==0:
            explore(adj,adj[i],CCnum,visited,num)
            num+=1
    return num-1

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
    print(reach(adj))
