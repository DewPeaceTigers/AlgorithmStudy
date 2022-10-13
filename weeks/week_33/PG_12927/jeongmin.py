"""
야근 지수를 최소화 > 남은 일의 작업량 최대값 줄이기!!
"""

import heapq

def solution(n, works):
    answer = 0
    
    wq = []
    for work in works:
        heapq.heappush(wq, -work)
    
    for i in range(n):
        # 만약 큐가 비어있다면 작업 완료!
        if not wq:
            break
        
        w = heapq.heappop(wq)
        
        # 남은 작업량이 1보다 큰 경우
        if w < -1:
            heapq.heappush(wq, w+1)
    
    # 야근 지수 계산
    for x in wq:
        answer += x**2
    
    return answer