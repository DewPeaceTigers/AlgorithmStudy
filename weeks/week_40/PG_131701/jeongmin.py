# 원형 수열의 연속 부분 수열 합으로 만들 수 있는 수의 개수
# 연속 부분 수열 (1개~n개) => 조합 사용하면 안됨 => 순서 고정!


def solution(elements):
    answer = 0
    
    # 원소의 개수
    N = len(elements)
    
    # 원형 수열의 연속 부분 수열 합으로 만들 수 있는 수의 개수
    sum_set = set()
    
    # 부분 수열 (원소 1개~N개) 확인
    for cnt in range(1, N+1):
        for i in range(N):
            # 부분 수열 
            sub_seq = []
            
            if i+cnt <= N:
                sub_seq = elements[i:i+cnt]
            else:
                sub_seq = elements[i:]+ elements[:(i+cnt)%N]

            # 부분 수열의 합 저장
            sum_set.add(sum(sub_seq))

    answer = len(sum_set)
    
    return answer