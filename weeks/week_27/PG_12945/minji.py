def solution(n):
    answer = 0
    if n==1:
        return 1
    
    if n==2:
        return 2
    a=1
    b=2
    for i in range(3, n) :
        a, b=b, (a+b)%1234567
    return b