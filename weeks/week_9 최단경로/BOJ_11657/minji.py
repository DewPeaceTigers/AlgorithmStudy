import sys

INF=sys.maxsize
N, M=map(int, sys.stdin.readline().split())
graph=[]
for i in range(M) :
    a, b, c=map(int, sys.stdin.readline().split())
    graph.append([a, b, c])
dist=[INF]*(N+1)
def bf(start):
    dist[start]=0
    for i in range(N):
        for j in range(M) :
            node=graph[j][0]
            next_node=graph[j][1]
            cost=graph[j][2]
            if dist[node]!=INF and dist[next_node] > dist[node]+cost:
                dist[next_node]=dist[node]+cost
                if i==N-1:
                    return True

    return False
negative_cycle=bf(1)

if negative_cycle:
    print('-1')
else:
    for i in range(2, N+1):
        if dist[i]==INF:
            print('-1')
        else:
            print(dist[i])