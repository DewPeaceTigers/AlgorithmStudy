def solution(n):
    answer = 0
    
    dp = [1]*(n+1)
    
    for i in range(2, n+1):
        dp[i] = (dp[i-2]+dp[i-1])%1234567
    
    answer = dp[n]
    
    return answer