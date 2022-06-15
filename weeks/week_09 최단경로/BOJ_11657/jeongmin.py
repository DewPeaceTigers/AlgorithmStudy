''' [풀이]
1번 도시에서 출발해서 나머지 도시로 가는 가장 빠른 시간을 구하는 프로그램
(A는 시작도시, B는 도착도시, C는 버스를 타고 이동하는데 걸리는 시간)
- C가 음수인 경우도 있으므로 벨만-포드 알고리즘 이용
'''

import sys
input= sys.stdin.readline
INF = int(1e9)

# 도시의 개수 N (1 ≤ N ≤ 500), 버스 노선의 개수 M (1 ≤ M ≤ 6,000) 입력
N, M = map(int, input().split())

graph = [[]*(N+1) for _ in range(N+1)]

for _ in range(M):
  # 시작도시, 도착도시, 걸리는 시간
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  

dist = [INF]* (N+1)
def bf(start):
  dist[start] = 0

  for i in range(N): # N번의 단계 반복
    for cur in range(1, N+1): # 모든 간선 확인
      for g in graph[cur]:
        if dist[cur] != INF and dist[g[0]]> dist[cur]+g[1]:
          dist[g[0]] = dist[cur]+g[1]

          # 음수 사이클 판별
          if i==N-1:
            return True

  return False

n_cycle = bf(1)
# print(n_cycle)
# print(dist)
if n_cycle:
  print(-1)
else:
  for d in dist[2:]:
    if d==INF:
      print(-1)
    else:
      print(d)