import sys

INF=sys.maxsize
n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
cost=[[INF]*n for _ in range(n)]
for i in range(m) :
    a, b, c=map(int, sys.stdin.readline().split())
    if cost[a-1][b-1]>c :
        cost[a-1][b-1]=c

for k in range(n) :
    for i in range(n) :
        for j in range(n) :
            if i != j and cost[i][j] > cost[i][k]+cost[k][j] :
                cost[i][j]=cost[i][k]+cost[k][j]

for i in cost :
    for j in i :
        if j == INF :
            print(0, end=' ')
        else :
            print(j, end=' ')
    print()