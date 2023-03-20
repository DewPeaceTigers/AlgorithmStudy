def solution(x, y, n):
    if x==y : return 0
    dp = [int(1e9)]*(y+1)
    dp[x] = 0
    for i in range(x+1,y+1):
        dp[i] = dp[i-n]
        if i%2==0:
            dp[i] = min(dp[i//2],dp[i])
        if i%3==0:
            dp[i] = min(dp[i//3],dp[i])
        dp[i]+=1
    return dp[-1] if dp[-1]<(int(1e9)+1) else -1