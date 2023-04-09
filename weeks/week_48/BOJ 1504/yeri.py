import sys
from collections import defaultdict,deque
import heapq
input = sys.stdin.readline

N, E = map(int,input().split())
lines = []
graph = defaultdict(list)
for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a-1].append((b-1,c))
    graph[b-1].append((a-1,c))

v1,v2 = map(int,input().split())
v1-=1
v2-=1

def dijkstra(s,e):
    heap = [[s,0]]
    dp = [int(1e9)]*N
    dp[s]=0
    while heap:
        now, cost = heapq.heappop(heap)
        for next, price in graph[now]:
            if cost+price < dp[next]:
                heapq.heappush(heap,[next,cost+price])
                dp[next]=cost+price
    return dp[e]
path_v1 = dijkstra(0,v1)+dijkstra(v1,v2)+dijkstra(v2,N-1)
path_v2 = dijkstra(0,v2)+dijkstra(v2,v1)+dijkstra(v1,N-1)

answer = min(path_v1,path_v2)
if answer< int(1e9): print(answer)
else: print(-1)