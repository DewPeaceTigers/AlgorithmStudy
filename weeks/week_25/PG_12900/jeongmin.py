# 규칙을 찾으면 피보나치 수열을 구하는 것과 같음!!
def solution(n):    
    x1, x2 = 1, 1

    for i in range(1, n):
        x1, x2 = x2, (x1+x2)%1000000007
        
    answer = x2
        
    return answer