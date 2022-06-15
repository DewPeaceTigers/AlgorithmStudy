''' [풀이]
주어진 시작점(u)에서 다른 모든 정점(v)으로의 최단 경로를 구하는 프로그램
- u에서 v로 가는 가중치 w는 10 이하의 자연수
- 가중치가 자연수이므로 다익스트라 알고리즘 이용
'''

import sys
input= sys.stdin.readline
import heapq # 우선순위 큐 사용

# 정점의 개수 V와 간선의 개수 E (1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000) 입력
V, E = map(int, input().split())

# 시작 정점 번호 K(1 ≤ K ≤ V) 입력
K = int(input())

# 인접리스트 형태로 저장
graph = [[] for _ in range(V+1)]
for i in range(E):
  u, v, w = map(int, input().split())
  graph[u].append((v, w))
  
# 각 정점으로의 거리 저장
INF = int(1e9)
d = [INF]*(V+1)

# 시작점 거리 0
d[K] = 0

pq =[] # (가중치, 끝점)

heapq.heappush(pq, (0, K))

while pq:
  w, v = heapq.heappop(pq)

  for g in graph[v]:
    if d[g[0]] > d[v]+g[1]:
      d[g[0]] = d[v]+g[1]
      heapq.heappush(pq, (d[g[0]], g[0]))

for i in range(1, V+1):
  if d[i] ==INF:
    print("INF")
  else:
    print(d[i])