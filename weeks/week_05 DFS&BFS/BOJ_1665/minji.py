'''
못품
인터넷 서치 방법
1. leftheap과 rightheap에 번갈아서 넣어주고 중간값 출력되게
leftheap은 최대힙, rightheap은 최소힙으로
'''

import heapq
import sys

leftheap=[]
rightheap=[]
n=int(input())

for i in range(n) :
    num=int(sys.stdin.readline())
    if len(leftheap) == len(rightheap) :
        heapq.heappush(leftheap, -num)
    else:
        heapq.heappush(rightheap, num)
    #rightheap에 원소 넣는 차례에 leftheap보다 작은 값을 넣게 되면
    #rightheap에 중간값보다 큰 원소가 들어가게 되므로 두 힙의 첫 원소 교체
    if rightheap and rightheap[0] < -leftheap[0] :
        l_value=heapq.heappop(leftheap)
        r_value=heapq.heappop(rightheap)

        heapq.heappush(leftheap, -r_value)
        heapq.heappush(rightheap, -l_value)
    print(-leftheap[0])
