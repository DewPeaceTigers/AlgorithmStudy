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

def makeParent(vertex):
    for v in vertex:
        parent[v]=v
        rank[v]=0

V,E = map(int,input().split())
lands=list()
vertex=list()
edges=list()

parent.clear()
rank.clear()
for i in range(E):
    a,b,c=map(int,input().split())
    edges.extend([(c,a,b),(c,b,a)])
    vertex.extend([a,b])

makeParent(vertex)
edges.sort()

mst=list()
for edge in edges:
    weight,node1,node2=edge
    if find(node1)!=find(node2):
        union(node1,node2)
        mst.append(edge)

print(sum([w for w,_,_ in mst]))