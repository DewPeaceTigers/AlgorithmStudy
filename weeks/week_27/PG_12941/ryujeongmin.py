def solution(A,B):
    answer = 0

    # A는 오름차순, B는 내림차순
    A.sort()
    # B.sort(reverse=True)
    B.reverse()

    for i in range(len(A)):
        answer += A[i]*B[i]
    
    return answer