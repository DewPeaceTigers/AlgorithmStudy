#75%에서
import sys
import heapq

input=sys.stdin.readline

n, e=map(int, input().split())

graphs=[[] for _ in range(n+1)]
for _ in range(e) :
    a, b, c=map(int, input().split())
    graphs[a].append([b, c])
    graphs[b].append([a, c])

v1, v2=map(int, input().split())

def dijkstra(start) :
    heap=[]
    heapq.heappush(heap, [0, start])
    visit=[float('inf')]*(n+1)
    visit[start]=0

    while heap:
        cost, now=heapq.heappop(heap)
        for next, weight in graphs[now] :
            if visit[next]>cost+weight :
                visit[next]=cost+weight
                heapq.heappush(heap, [cost+weight, next])

    return visit

one=dijkstra(1)
v1_distance=dijkstra(v1)
v2_distance=dijkstra(v2)

answer=min(one[v1]+v1_distance[v2]+v2_distance[n], one[v2]+v2_distance[v1]+v1_distance[n])

if answer==float('inf') :
    print(-1)
else:
    print(answer)
