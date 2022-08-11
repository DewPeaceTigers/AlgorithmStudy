def solution(n):
    a,b=0,1
    for i in range(2,n+1):
        a,b = b, (a+b)%1234567
    return b