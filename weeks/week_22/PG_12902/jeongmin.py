"""
풀이 찾아봄..
규칙성 : f(n) = f(n-2) x 3 + f(n-4) x 2 + … + f(2) x 2 + 2
> f(n) = 4*f(n-2) - f(n-4)
"""

def solution(n):
    answer = 0
    
    # 짝수인 경우
    if n%2==0:
        dp = [0]*(n//2+1)
        dp[1], dp[2] = 3, 11
        
        for i in range(3, n//2+1):
            dp[i] = (4*dp[i-1]-dp[i-2])%1000000007
        
        answer = dp[n//2]
        
    return answer