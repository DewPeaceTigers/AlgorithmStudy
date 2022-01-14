''' [풀이]
heapq 사용 (heapq 는 기본적으로 최소 힙!)
  - x 값 추가: heapq.heappush(q, x)
  - 가장 작은 값 출력 후 제거: heapq.heappop(q)
  - 비어있는 경우 : len(minHeap) ==0 일 때
'''

import heapq
import sys

input =sys.stdin.readline

# 연산의 개수 N(1 ≤ N ≤ 100,000) 입력
N = int(input())

# 우선순위 큐
minHeap =[]

for _ in range(N):
  n= int(input())

  # n이 자연수이면
  if n:
    # default는 최소 힙
    heapq.heappush(minHeap, n)

  # n이 0이면
  else:
    if len(minHeap):
      print(heapq.heappop(minHeap))
    # 우선순위 큐가 비어있는 경우
    else:
      print(0)