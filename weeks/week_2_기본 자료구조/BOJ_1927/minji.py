import heapq
import sys
n = int(sys.stdin.readline())

heap = []
for i in range(n) :
    n = int(sys.stdin.readline())
    if n == 0 :
        if len(heap) == 0 :
            print(0)
        else :
            print(heapq.heappop(heap))
    else :
        heapq.heappush(heap, n)
