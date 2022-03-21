"""
1이 비용이라 n-1이 답이다..
"""
import sys
input=sys.stdin.readline

T=int(input())
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

for _ in range(T):
    N,M=map(int,input().split())
    lands=set()
    edges=list()

    parent.clear()
    rank.clear()
    for _ in range(M):
        edges.append(list(map(int,input().split())))
        lands.add(edges[-1][0])
        lands.add(edges[-1][1])
    makeParent(lands)

    mst=list()
    for edge in edges:
        node1,node2=edge
        if find(node1)!=find(node2):
            union(node1,node2)
            mst.append(edge)
    print(len(mst))