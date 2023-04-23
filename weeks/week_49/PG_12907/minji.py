def solution(n, money):
    answer = 0
    dp=[1]+[0]*n
    for coin in money :
        for i in range(coin, n+1) :
            if i>=coin :
                dp[i]+=dp[i-coin]
    return dp[n]%1000000007