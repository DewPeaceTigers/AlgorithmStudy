''' [풀이]
선을 하나 이을 때마다 두 별 사이의 거리만큼의 비용이 든다고 할 때, 별자리를 만드는 최소 비용을 구하시오.
-> 각 정점을 기준으로 ? 프림 알고리즘 사용 
'''

import sys
input = sys.stdin.readline
import math
import heapq

# 별의 개수 n(1 ≤ n ≤ 100) 입력
n = int(input())

stars = []
for _ in range(n):
  # x, y 좌표 입력
  x, y = map(float, input().split())
  stars.append((x, y))
  
# 후보 별자리
candidates = [i for i in range(n)]

def prim(start):
  ans = 0
  q =[]
  heapq.heappush(q, (0, 0))

  while q:
    d, idx = heapq.heappop(q)

    if idx in candidates:
      candidates.remove(idx) # 후보에서 제거
      ans += d
    # print(d, idx, candidates)

    x1, y1 = stars[idx]
    for c in candidates:
      x2, y2 = stars[c]
      d = round(math.sqrt((x2-x1)**2+(y2-y1)**2),2)
      heapq.heappush(q, (d, c))
      
  return ans
  
print(prim(0))