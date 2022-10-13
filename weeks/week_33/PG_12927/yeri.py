import heapq
def solution(n, works):
    answer = 0
    q=[]
    for work in works:
        heapq.heappush(q,-work)
    while n!=0 and q:
        work = -heapq.heappop(q)
        if work-1!=0:
            heapq.heappush(q,-(work-1))
        n-=1
    for work in q:
        answer+= (-work)**2
                
    return answer