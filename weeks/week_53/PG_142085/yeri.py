import heapq
def solution(n, k, enemy):
    answer = len(enemy)
    heap = []
    for i,en in enumerate(enemy):
        # k를 일단 쓴다고 가정
        heapq.heappush(heap, en)
        if k<len(heap):
            n-= heapq.heappop(heap)
        if n <=0:
            answer = i
            break
    
    return answer
