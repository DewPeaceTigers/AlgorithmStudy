import heapq
import sys
n = int(sys.stdin.readline())
q = []
for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(q) == 0:
            print(0)
        else:
            print(abs(heapq.heappop(q)))
    else:
        heapq.heappush(q, -x)
        # heapq는 기본적으로 최소 힙으로, 음수로 바꿔 넣어서 최소 힙으로 정렬되면 값들을 절대값을 씌우게 되면 최대힙이 된다.
        # 기본 가정은 원소 값들이 자연수여야 할 것 같다.
# https://steadily-worked.tistory.com/674