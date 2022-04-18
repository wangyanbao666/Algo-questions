#Uses python3

import sys

def add_component(adj,ls,com,visited):
    for i in ls:
        if visited[i]==0:
            com.append(i)
            visited[i]=1
            add_component(adj,adj[i],com,visited)


def number_of_components(adj,u,v):
    result = 0
    component=[]
    visited=[0]*len(adj)
    add_component(adj,adj[u],component,visited)
    #write your code here
    if v in component:
        result=1
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    # input=input()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    # print(n,m)
    data = data[2:]
    # print(data)
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj,data[-2]-1,data[-1]-1))

# 4 4 1 2 3 2 4 3 1 4 1 4