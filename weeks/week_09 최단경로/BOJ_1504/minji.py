'''
1->v1->n
1->v2->n
두개 중 최단거리
'''
import heapq
import sys

INF=sys.maxsize
N, E=map(int, sys.stdin.readline().split())
graph=[[] for _ in range(N+1)]

for i in range(E) :
    a, b, c=map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2=map(int, sys.stdin.readline().split())

def dijkstra(start):
    d=[INF]*(N+1)
    queue=[]
    d[start]=0
    heapq.heappush(queue, [0, start])
    while queue:
        w, node=heapq.heappop(queue)
        for next_node, wei in graph[node] : #현재 노드에서 갈 수 있는 노드와 가중치
            next_wei=wei+w
            if d[next_node]>next_wei: #새로운 가중치가 더 작으면 갱신
                d[next_node]=next_wei
                heapq.heappush(queue, [next_wei, next_node])
    return d

one=dijkstra(1)
v1_dijkstra=dijkstra(v1)
v2_dijkstra=dijkstra(v2)

answer=min(one[v1]+v1_dijkstra[v2]+v2_dijkstra[N], one[v2]+v2_dijkstra[v1]+v1_dijkstra[N])

if answer < INF :
    print(answer)
else:
    print(-1)