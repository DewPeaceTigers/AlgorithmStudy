def solution(n):
    answer = 0
    
    a, b = 0, 1
    for i in range(1, n):
        a, b = b, (a+b)%1234567
    
    answer = b
    
    return answer