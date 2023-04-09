# 임의로 주진 두 정점은 반드시 통과하기
# 한 번 이동했던 정점, 이동했던 간선도 다시 이동 가능
# 반드시 최단 경로로 이동해야 함!

# 두 정점 a, b
# 1 -> a -> b -> N
# 1 -> b -> a -> N 비교?
import heapq
import sys

input = sys.stdin.readline

N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, input().split())


def dijkstra(start):
    dp = [1e9 for i in range(N + 1)]
    dp[start] = 0
    q = []
    heapq.heappush(q, [0, start])
    while q:
        w, x = heapq.heappop(q)
        for to, nw in graph[x]:
            weight = nw + w
            if dp[to] > weight:
                dp[to] = weight
                heapq.heappush(q, [weight, to])
    return dp


v = [dijkstra(1), dijkstra(v1), dijkstra(v2)]

cnt = min(v[0][v1] + v[1][v2] + v[2][N], v[0][v2] + v[2][v1] + v[1][N])
print(cnt if cnt < 1e9 else -1)
