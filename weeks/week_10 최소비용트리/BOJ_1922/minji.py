import sys

N=int(input())
M=int(input())

total_cost=0
edges=[]
parent=[i for i in range(N+1)]

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

for i in range(M):
    a, b, c=map(int, sys.stdin.readline().split())
    edges.append((c, a, b))

edges.sort()
for i in edges:
    cost, a, b=i
    if find(a) != find(b):
        union(a, b)
        total_cost+=cost

print(total_cost)