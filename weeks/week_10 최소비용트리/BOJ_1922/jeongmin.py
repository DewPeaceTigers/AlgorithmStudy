''' [풀이]
최소 스패닝 트리 구하기
- 크루스칼 / 프림 알고리즘 사용
'''

import sys
input = sys.stdin.readline

# 컴퓨터의 수 N (1 ≤ N ≤ 1000) 입력
N = int(input())
# 간선의 개수 E(1 ≤ E ≤ 100,000) 입력
M = int(input())

edges = []
# 간선 정보 입력
for _ in range(M):
  a, b, c = map(int, input().split())
  if a!=b:
    edges.append((c, a, b)) # 가중치, 정점1, 정점2

parent = [i for i in range(N+1)]

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

edges.sort()

ans = 0
for edge in edges:
  weight, a, b = edge

  pa = find_parent(parent, a)
  pb = find_parent(parent, b)
  # a, b가 부모가 같지 않으면
  if pa!= pb:
    # 합치기
    union(parent, a, b)
    ans += weight

print(ans)