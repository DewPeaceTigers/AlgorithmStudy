def solution(sequence, k):
    # 부분 수열의 시작 인덱스, 마지막 인덱스
    answer = [0, 1e9]
    
    N = len(sequence)
    s = 0
    
    sum_seq = 0
    
    for i in range(N):
        sum_seq += sequence[i]
        
        if sum_seq < k:
            continue
        
        # 부분 수열의 합이 k보다 크다면 시작 인덱스 증가
        while sum_seq > k:
            sum_seq -= sequence[s]
            s += 1
        
        # 합이 k인 부분 수열이 여러 개인 경우 길이가 짧은 수열
        if sum_seq == k and (i-s) < (answer[1]-answer[0]):
            answer = [s, i]
            
    return answer