def solution(A,B):
    A.sort()
    B.sort(reverse = True)
    return sum([A[i]*B[i] for i in range(len(A))])