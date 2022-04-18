#Uses python3

import sys

sys.setrecursionlimit(200000)

def dfs(adj, used, order, x):
    global num
    #write your code here
    used[x]=1
    for i in adj[x]:
        if used[i]==0:
            dfs(adj,used,order,i)
    order.append(x)

def toposort(adj):
    used = [0] * len(adj)
    order = []
    #write your code here
    for i in range(len(adj)):
        if used[i]==0:
            dfs(adj, used, order, i)
    return reversed(order)

def explore(index,adj,visited):
    visited[index]=1
    for i in adj[index]:
        if visited[i]==0:
            visited[i]=1
            explore(i,adj,visited)

def number_of_strongly_connected_components(adj,adj_rev):
    result = 0
    #write your code here
    reverse_order=toposort(adj_rev)
    a=list(reverse_order)
    # print(a)
    visited=[0]*len(adj)
    for i in a:
        # print(i)
        if visited[i]==0:
            explore(i,adj,visited)
            result+=1
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    # input=input()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    adj_rev = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    for (a,b) in edges:
        adj_rev[b-1].append(a-1)
    # print(adj)
    print(number_of_strongly_connected_components(adj,adj_rev))

# 4 4 1 2 4 1 2 3 3 1
# 5 7 2 1 3 2 3 1 4 3 4 1 5 2 5 3
# 10 20 7 8 4 10 3 2 1 3 4 9 2 6 8 3 8 2 6 1 6 10 10 6 1 4 3 8 1 5 8 9 5 3 3 4 5 1 8 5 8 4