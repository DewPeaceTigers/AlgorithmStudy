def solution(a):
    answer = 0
    
    N = len(a)
    
    # a[i] 기준으로 [왼쪽 최솟값, 오른쪽 최솟값] 저장
    min_num = [[1e9, 1e9] for _ in range(N)]
    
    left_min = 1e9
    right_min = 1e9
    for i in range(N):
        left_min = min(left_min, a[i])
        right_min = min(right_min, a[N-1-i])
        
        min_num[i][0] = left_min
        min_num[N-1-i][1] = right_min
    # print(min_num)
    
    # 왼쪽의 최솟값, 오른쪽 부분 최솟값보다 모두 큰 경우에만 최후에 남을 수 없음
    for i in range(N):
        if min_num[i][0]< a[i] and min_num[i][1] < a[i]:
            continue
            
        answer += 1
    
    return answer