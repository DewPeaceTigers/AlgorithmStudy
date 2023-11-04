from collections import deque
def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    A, B = deque(A),deque(B)
    
    while B:
        # 이기는 패만 남기기
        if A[0] < B[0]:
            answer+=1
            A.popleft()
            B.popleft()
        else:
            B.popleft()
    return answer