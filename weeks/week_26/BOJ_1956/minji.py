import sys

INF=sys.maxsize
input=sys.stdin.readline
v, e=map(int, input().split())

boards=[[INF]*v for _ in range(v)]
for _ in range(e) :
    a, b, c=map(int, input().split())
    boards[a-1][b-1]=c
    
for k in range(v) :
    for i in range(v) :
        for j in range(v) :
            boards[i][j]=min(boards[i][j], boards[i][k]+boards[k][j])
            
answer=INF
for i in range(v) :
    answer=min(answer, boards[i][i])
    
if answer==INF :
    print(-1)
else:
    print(answer)