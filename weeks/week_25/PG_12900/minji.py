def solution(n):
    answer = 0
    dp=[0]*n
    dp[0]=1
    dp[1]=2
    for i in range(2, n) :
        dp[i]=(dp[i-2]+dp[i-1])%1000000007
    return dp[n-1]