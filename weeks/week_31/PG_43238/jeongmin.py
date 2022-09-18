# 모든 사람이 심사를 받는데 걸리는 시간을 최소로 하기!
def solution(n, times):
    answer = 0
    
    INF = int(1e9 * 1e9)
    
    start, end = 0, INF
    
    while start<= end:
        mid = (start + end) // 2
        
        people = 0
        
        # 누적합 구하기
        for time in times:
            people += mid//time
        
        if people >= n:
            answer = mid
            end = mid - 1
            
        else:
            start = mid + 1
            
    return answer