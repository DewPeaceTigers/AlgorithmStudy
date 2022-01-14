''' [풀이]
heapq 사용 (heapq 는 기본적으로 최소 힙!)
최대 힙을 구현하기 위해서는 요소에 음수 부호(-)를 붙여서 사용
  - x 값 추가: heapq.heappush(q, -x)
  - 가장 작은 값 출력 후 제거: -heapq.heappop(q)
  - 비어있는 경우 : len(minHeap) ==0 일 때
'''

import heapq
import sys

input = sys.stdin.readline

# N(1 ≤ N ≤ 100,000) 입력
N = int(input())

# 우선순위 큐
q = []

for _ in range(N):
  n= int(input())

  # n이 자연수이면
  if n:
    # default는 최소 힙
    # 최대 힙 -> - 붙여서 저장
    heapq.heappush(q, -n)

  # n이 0이면
  else:
    # 우선순위 큐가 비어있는 경우
    if len(q)==0:
      print(0)
    else:
      print(-heapq.heappop(q))