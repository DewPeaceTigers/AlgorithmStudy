import sys
input=sys.stdin.readline
n, m=map(int, input().split())

relationships=[[float('inf')]*n for _ in range(n)]
for _ in range(m) :
    a, b=map(int, input().split())
    relationships[a-1][b-1]=1
    relationships[b-1][a-1]=1

for k in range(n) :
    for i in range(n) :
        for j in range(n) :
            relationships[i][j]=min(relationships[i][k]+relationships[k][j], relationships[i][j])

cost=float('inf')
ans=0
for i in range(n) :
    if(cost>sum(relationships[i])) :
        cost=sum(relationships[i])
        ans=i
print(ans+1)