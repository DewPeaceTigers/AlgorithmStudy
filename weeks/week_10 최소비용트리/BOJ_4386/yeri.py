import sys,math
input=sys.stdin.readline

parent=dict()
rank=dict()

def find(node):
    if parent[node]!=node:
        parent[node]=find(parent[node])
    return parent[node]

def union(node1,node2):
    root1=find(node1)
    root2=find(node2)

    if rank[root1]> rank[root2]:
        parent[root2]=root1
    else:
        parent[root1]=root2
        if rank[root1] == rank[root2]:
            rank[root2]+=1

def makeParent(lands):
    for land in lands:
        parent[land]=land
        rank[land]=0

N=int(input())
lands=list()
vertex=list()
edges=list()

parent.clear()
rank.clear()
for i in range(N):
    n1,n2=map(float,input().split())
    lands.append((i,n1,n2))
    vertex.append(i)

for i in range(N):
    for j in range(i+1,N):
        edges.append((math.sqrt((lands[i][1]-lands[j][1])**2+(lands[i][2]-lands[j][2])**2),lands[i][0],lands[j][0]))
makeParent(vertex)
edges.sort()

mst=list()
for edge in edges:
    weight,node1,node2=edge
    if find(node1)!=find(node2):
        union(node1,node2)
        mst.append(edge)

sums=0
for w, _, _ in mst : sums+=w

print(round(sums,2))