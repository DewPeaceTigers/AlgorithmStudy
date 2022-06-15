'''[풀이]
계속 시간초과.. 답 찾아봄!!

힙을 두 개 써서 n을 분배할 수 있다.
왼쪽 힙은 최대 힙으로 정렬하고, 오른쪽 힙은 최소 힙으로 정렬하면
왼쪽 힙의 첫번째 요소는 항상 중앙값이 된다.
'''

import sys
import heapq
input = sys.stdin.readline

n = int(input())
max_h, min_h = [], []

for i in range(n):
    num = int(input())
    # 왼쪽 힙과 오른쪽 힙의 길이가 같으면 (요소 * -1) 을 왼쪽 힙에 삽입
    if len(max_h) == len(min_h):
        heapq.heappush(max_h, -num)
    # 그렇지 않으면 오른쪽 힙에 삽입
    else:
        heapq.heappush(min_h, num)

    # 왼쪽 힙과 오른쪽 힙에 요소가 존재하고, 왼쪽 힙의 (첫번째 요소* -1) 가 오른쪽 첫번째 요소보다 클 때
    if len(max_h) >= 1 and len(min_h) >= 1 and max_h[0] * -1 > min_h[0]:
        # 왼쪽 힙의 첫번째 요소와 오른쪽 힙의 첫번째 요소를 바꿔줌
        max_value = heapq.heappop(max_h) * -1
        min_value = heapq.heappop(min_h)
        
        heapq.heappush(max_h, min_value * -1)
        heapq.heappush(min_h, max_value)

    # 왼쪽 힙의 (첫번째 요소 * -1)를 출력
    print(max_h[0] * -1)