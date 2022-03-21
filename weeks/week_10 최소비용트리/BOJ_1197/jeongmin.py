''' [풀이]
최소 스패닝 트리 구하기
- 크루스칼 / 프림 알고리즘 사용
'''

import sys
input = sys.stdin.readline
import heapq

# 정점의 개수 V(1 ≤ V ≤ 10,000), 간선의 개수 E(1 ≤ E ≤ 100,000) 입력
V, E = map(int, input().split())

edges = []
# 간선 정보 입력
for _ in range(E):
  a, b, c = map(int, input().split())
  edges.append((c, a, b)) # 가중치, 정점1, 정점2
  # edges.append((c, a, b)) # 가중치, 정점1, 정점2

parent = [i for i in range(V+1)]

def find_parent(parent, x):
  if parent[x]!= x:
    parent[x] = find_parent(parent, parent[x])

  return parent[x]

def union(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  # 더 작은 노드로 부모 합치기
  if a<b:
    parent[b] = a
  else:
    parent[a] = b

heapq.heapify(edges)

ans = 0
while edges:
  weight, a, b = heapq.heappop(edges)

  pa = find_parent(parent, a)
  pb = find_parent(parent, b)
  # a, b가 부모가 같지 않으면
  if pa!= pb:
    # 합치기
    union(parent, a, b)
    ans += weight

print(ans)