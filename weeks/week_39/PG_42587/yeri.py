from collections import deque
import heapq
def solution(priorities, location):
    q = deque()
    heap = []
    for i,priority in enumerate(priorities):
        q.append([priority,i])
        heapq.heappush(heap,-priority)
    answer = 0
    while q:
        front,idx = q.popleft()
        if front < -heap[0]:
            q.append([front,idx])
        elif front == -heap[0]:
            heapq.heappop(heap)
            answer+=1
            if idx == location:
                break
    return answer