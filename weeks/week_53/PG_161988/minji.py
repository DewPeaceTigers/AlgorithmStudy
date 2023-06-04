def solution(sequence):
    dp=[[0, 0] for _ in range(len(sequence))]
    
    dp[0][0]=sequence[0]
    dp[0][1]=sequence[0]*-1
    
    answer=max(dp[0][0], dp[0][1])
    
    for idx in range(1, len(sequence)):
        if idx%2==0 :
            dp[idx][1]=max(dp[idx-1][1], 0)+(sequence[idx]*-1)
            dp[idx][0]=max(dp[idx-1][0], 0)+sequence[idx]
        else:
            dp[idx][1]=max(dp[idx-1][1], 0)+sequence[idx]
            dp[idx][0]=max(dp[idx-1][0], 0)+(sequence[idx]*-1)
        answer=max(answer, max(dp[idx]))
    return answer
