import sys

input=sys.stdin.readline

n, m, k=map(int, input().split())
costs=[0]+list(map(int, input().split()))

parents=[x for x in range(n+1)]

def find(node) :
    if parents[node]!=node :
        parents[node]=find(parents[node])

    return parents[node]

def union(node1, node2):
    root1=find(node1)
    root2=find(node2)

    if root1!=root2 :
        if costs[a] <= costs[b] :
            parents[b]=a
        else:
            parents[a]=b


for _ in range(m) :
    a, b=map(int, input().split())
    union(a, b)

ans=0
for idx, root in enumerate(parents):
    if idx==root :
        ans+=costs[root]

if ans<=k :
    print(ans)
else:
    print("Oh no")