import sys

V, E=map(int, input().split())
edges=[]
total_cost=0
parent=[i for i in range(V+1)]
for i in range(E):
    A, B, C=map(int, sys.stdin.readline().split())
    edges.append((C, A, B))

edges.sort()

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a, b):
    root1=find(a)
    root2=find(b)
    if root1<root2:
        parent[root2]=root1
    else:
        parent[root1]=root2

for edge in edges:
    cost, a, b=edge
    if find(a) != find(b):
        union(a, b)
        total_cost+=cost
print(total_cost)