import sys
input = sys.stdin.readline

N,M=map(int,input().split())
bus_lines=[]
for _ in range(M):
    a,b,c=map(int,input().split())
    bus_lines.append((a,b,c))
INF=10000*N+1
dist=[INF]*(N+1)
dist[1]=0
for i in range(N):
    for a,b,c in bus_lines: # 각 노드마다 모든 간선을 확인
        if dist[a]!=INF and dist[b] > dist[a]+c:
            if i == N-1:
                print(-1)
                sys.exit()
            dist[b]=dist[a]+c

for i in range(2,N+1):
    if dist[i]==INF : print(-1)
    else: print(dist[i]) 