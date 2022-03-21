"""
a==b일 때는 제외하도록 처리.
"""
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

V = int(input())
E = int(input())

lands=list()
vertex=list()
edges=list()

parent.clear()
rank.clear()
for i in range(E):
    a,b,c=map(int,input().split())
    if a==b : continue
    edges.extend([(c,a,b),(c,b,a)])
    vertex.extend([a,b])

# for i in range(N):
#     for j in range(i+1,N):
#         edges.append((math.sqrt((lands[i][1]-lands[j][1])**2+(lands[i][2]-lands[j][2])**2),lands[i][0],lands[j][0]))
makeParent(vertex)
edges.sort()

mst=list()
for edge in edges:
    weight,node1,node2=edge
    if find(node1)!=find(node2):
        union(node1,node2)
        mst.append(edge)


print(sum([w for w,_,_ in mst]))