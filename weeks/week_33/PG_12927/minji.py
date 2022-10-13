'''
풀이 참고
'''
import heapq

def solution(n, works):
    answer = 0
    if n>=sum(works) :
        return 0
    works=[-w for w in works]
    heapq.heapify(works)
    for _ in range(n) :
        i=heapq.heappop(works)
        i+=1
        heapq.heappush(works, i)
    return sum([w ** 2 for w in works])