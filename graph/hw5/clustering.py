#Uses python3
import sys
import math

def find(i,parent):
    while parent[i]!=i:
        i=parent[i]
    return i

def union(u,v,parent,rank):
    u_root=find(u,parent)
    v_root=find(v,parent)
    if rank[u_root]>rank[v_root]:
        parent[v_root]=u_root
    else:
        parent[u_root]=v_root
        if rank[u_root]==rank[v_root]:
            rank[v_root]+=1


def clustering(x, y, k):
    num_of_tree=len(x)
    parent=[i for i in range(len(x))]
    rank=[0]*len(x)
    edges=[]
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            dis=math.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)
            edges.append([i,j,dis])

    while num_of_tree>=k:
        # print(1)
        dist=[i[2] for i in edges]
        m=dist.index(min(dist))
        s=edges.pop(m)
        u=s[0]
        v=s[1]
        u_root=find(u,parent)
        v_root=find(v,parent)
        if u_root!=v_root:
            union(u,v,parent,rank)
            num_of_tree-=1
            if num_of_tree==k-1:
                return s[2]



if __name__ == '__main__':
    input = sys.stdin.read()
    # input=input()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))

# 8 3 1 1 2 4 6 9 8 9 9 8 9 3 11 4 12 4
# 12 7 6 4 3 5 1 1 7 2 7 5 7 3 3 7 8 2 8 4 4 6 7 2 6 3