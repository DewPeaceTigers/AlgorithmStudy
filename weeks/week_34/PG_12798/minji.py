def solution(A, B):
    answer = 0
    A.sort()
    B.sort()

    for i in range(len(A) - 1, -1, -1):
        if (A[i] >= B[i]):
            tmp = B.pop(0)
            B.insert(i, tmp)
            print(B)

    for i in range(len(A)):
        if (A[i] < B[i]):
            answer += 1
    return answer
