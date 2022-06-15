import heapq
import sys

INF=sys.maxsize
V, E=map(int, sys.stdin.readline().split())
K=int(sys.stdin.readline())
graph=[[] for _ in range(V+1)]
d=[INF]*(V+1)
queue=[]
for i in range(E) :
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([v, w])

def Dijkstra(start):
    d[start]=0 #시작 정점에 해당하는 가중치는 0
    heapq.heappush(queue, [0, start]) #거리-노드 순으로 해야 정렬했을 때 가중치 순으로 됨

    while queue:
        min , node=heapq.heappop(queue)

        for next_node, wei in graph[node] :
            next_wei=wei+min 

            if next_wei < d[next_node] : #최소값 갱신
                d[next_node]=next_wei
                heapq.heappush(queue, [next_wei, next_node])


Dijkstra(K)
for i in d[1:] :
    print(i if i!=INF else "INF")