## 이해 못함
def solution(A, B):
    A.sort()
    B.sort()
    a = 0
    b = 0
    count = 0
    while a<len(A) and b<len(B):
        if A[a] < B[b]: 
            count+=1
            a+=1
        b+=1
    return count
            