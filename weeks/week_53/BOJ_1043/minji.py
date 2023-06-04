'''
진실을 이야기한 파티에 참석한 사람도 진실을 알게됨.
'''
import sys

input=sys.stdin.readline

n, m=map(int, input().split())

know=list(map(int, input().split()))[1:]

parent=[x for x in range(n+1)]
for k in know: #진실을 알고있는사람 0
    parent[k]=0

def find(x) :
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a, b) :
    a=find(a)
    b=find(b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b

participants=[]
ans=0
for _ in range(m) :
    p=list(map(int, input().split()))[1:]
    for i in range(len(p)-1) :
        union(p[i], p[i+1])
    participants.append(p)

for p in participants:
    for i in range(len(p)) :
        if find(p[i]) == 0 :
            break
    else:
        ans+=1

print(ans)