def solution(A, B):
    answer = 0
    
    # A와 B 오름차순 정렬
    A.sort()
    B.sort()
    
    # A와 B의 길이 저장
    n = len(B)
    
    # A의 원소와 비교할 B의 원소 인덱스값
    idx = 0
    
    for i in range(n):
        # A의 원소보다 큰 B의 원소 찾기
        while idx < n and A[i] >= B[idx]:
            idx += 1
        
        # 범위를 넘어간 경우
        if idx >= n:
            break
        
        answer += 1
        idx += 1
    
    return answer