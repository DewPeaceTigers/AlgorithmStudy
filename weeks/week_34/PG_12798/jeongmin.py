def solution(A, B):
    answer = -1
    
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    n = len(A)
    idx = 0
    
    for i in range(n):
        if A[i] < B[idx]:
            idx += 1
    
    answer = idx
    
    return answer