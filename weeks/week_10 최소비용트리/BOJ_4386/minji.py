import math

n=int(input())
stars=[]
distance=[]
total_cost=0
parent=[0]*(n+1)
for i in range(1, n+1):
    parent[i]=i

def find(parent, node):
    if parent[node]!=node:
        parent[node]=find(parent, parent[node])
    return parent[node]

def union(parent, node_a, node_b):
    root1=find(parent, node_a)
    root2=find(parent, node_b)
    if root1<root2:
        parent[root2]=root1
    else:
        parent[root1]=root2

for i in range(n):
    a, b=map(float, input().split())
    stars.append((a, b))

for i in range(n-1):
    for j in range(i+1, n):
        distance.append((math.sqrt((stars[i][0]-stars[j][0])**2+(stars[i][1]-stars[j][1])**2), i, j))

distance.sort()
for i in distance:
    cost, a, b=i
    if find(parent, a)!=find(parent, b):
        union(parent, a, b)
        total_cost+=cost

print(round(total_cost, 2))