import sys

T=int(input())
def find(parent, x):
    if parent[x]!=x:
        parent[x]=find(parent, parent[x])
    return parent[x]

def union(parent, node_v, node_e) :
    root1=find(parent, node_v)
    root2=find(parent, node_e)
    if root1<root2:
        parent[root2]=root1
    else:
        parent[root1]=root2

for i in range(T):
    edges=[]
    N, M = map(int, input().split())
    parent=[0]*(N+1)
    count=0
    for i in range(1, N+1):
        parent[i]=i

    for j in range(M):
        a, b=map(int, sys.stdin.readline().split())
        edges.append((a, b))
    edges.sort()
    for i in range(M):
        a, b=edges[i]
        if find(parent, a)!=find(parent, b):
            union(parent, a, b)
            count+=1
    print(count)

