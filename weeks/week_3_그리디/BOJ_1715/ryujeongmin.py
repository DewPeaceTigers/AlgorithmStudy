''' [풀이]
heapq 사용 
  - 크기가 작은 묶음부터 더해 나가야 최소값이 됨
  - 우선순위 큐 pq에 값이 2개 이상 있을 때 
    - 최솟값 2개를 꺼내 더한 후 더한 값을 우선순위 큐에 push 한다.
'''

import sys
import heapq

input= sys.stdin.readline

# 정렬된 숫자 카드 묶음의 개수 N (1 ≤ N ≤ 100,000) 입력
N = int(input())

# 숫자 카드 묶음의 각각의 크기 입력
pq = [int(input()) for _ in range(N)]
heapq.heapify(pq)

# 최소 비교 횟수 저장
ans =0

# 우선순위 큐 pq에 값이 2개 이상 있을 때 
while(len(pq)>1):
	# 최솟값 2개 pop
  sum = heapq.heappop(pq) + heapq.heappop(pq)

	# 두 묶음을 합치는 데 필요한 비교 횟수 더하기
  ans+= sum

	# 두 묶음을 합친 묶음 push
  heapq.heappush(pq, sum)

print(ans)