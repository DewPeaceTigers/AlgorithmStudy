def solution(n,times):
    # 시뮬레이션하기에는 1000000000으로 너무 많다
    # 이분탐색으로 시간을 정해두고 거기에 n을 처리할 수 있는지 확인하는 것이 더 빠르다
    times.sort()
    start,end = min(times),max(times)*n
    answer=0
    while start<=end:
        mid = (start+end)//2
        peop = 0
        for t in times:
            peop+=mid//t
        if peop >= n:
            answer=mid
            end = mid-1
        else:
            start = mid+1
    return answer