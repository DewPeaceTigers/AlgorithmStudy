## 못풀어서 같이 품

def solution(n, times):
    answer = 0
    times.sort() # 걸리는 시간 순으로 정렬
    # 심사관 수가 같거나 더 많은 경우
    start, end = min(times), max(times)*n
    while start<=end:
        mid = (start+end)//2
        # 가능한 사람 수 확인
        people =0
        for t in times:
            people += mid//t
        # 가능한 사람 수 >= n:
        if people >= n:
            answer = mid
            end = mid -1 # 시간 줄여보기
        else:
            start = mid+1 # 시간 늘리기
            
    return answer