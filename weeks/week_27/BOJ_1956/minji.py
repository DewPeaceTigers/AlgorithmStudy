import sys

INF=sys.maxsize
input=sys.stdin.readline
v, e=map(int, input().split())


graph=[[INF]*v for _ in range(v)]
for i in range(e) :
    a, b, c=map(int, input().split())
    graph[a-1][b-1]=c
    
for k in range(v) :
    for i in range(v) :
        for j in range(v) :
            graph[i][j]=min(graph[i][j], graph[i][k]+graph[k][j])

answer=INF          
for k in range(v) :
    answer=min(answer, graph[k][k])
    
if answer==INF :
    print(-1)
else:
    print(answer)