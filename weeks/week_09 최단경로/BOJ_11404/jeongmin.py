''' [풀이]
모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하는 프로그램
- 모든 경우에 대해 최소 거리를 구하는 것이므로 플로이드 워셜 알고리즘
'''

import sys
input= sys.stdin.readline
INF = int(1e9)

# 도시의 개수 n(2 ≤ n ≤ 100) 입력
n = int(input())

# 버스의 개수 m(1 ≤ m ≤ 100,000) 입력
m = int(input())

graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
  # 시작도시, 도착도시, 가는 비용
  a, b, c = map(int, input().split())
  if graph[a][b]>c:
    graph[a][b] = c

for i in range(1, n+1):
  graph[i][i] = 0
  
# for i in range(1, n+1):
#   for j in range(1, n+1):
#     if i!=j:
#       for k in range(1, n+1):
#         if i!=k and j!=k:
#         # graph[i][j]와 graph[i][k]+graph[k][j] 비교
#           graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])


for k in range(1, n+1): # 시작과 종료 사이에 끼어있는 노드(중간)
  for i in range(1, n+1): # 시작
    for j in range(1, n+1): # 종료
      if i!=j:
        graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(1, n+1):
  for j in range(1, n+1):
    if graph[i][j] ==INF:
      graph[i][j]=0
      
for i in range(1, n+1):
  print(*graph[i][1:])