def solution(sticker):
    answer = 0
    
    N = len(sticker)
    
    if N==1:
        return sticker[0]

    elif N==2:
        return max(sticker[0], sticker[1])
    
    # 뜯어낸 스티커에 적힌 숫자의 최대합
    n_sum = 0
    
    dp = [0]* N
    
    # 첫번째 스티커를 떼는 경우
    dp[1] = sticker[0]
    for i in range(2, N):
        dp[i] = max(dp[i-1], dp[i-2] + sticker[i-1])
    n_sum = dp[-1]
    
    # 첫번째 스티커를 떼지 않는 경우
    dp[1] = sticker[1]
    for i in range(2, N):
        dp[i] = max(dp[i-1], dp[i-2] + sticker[i])
    n_sum = max(dp[-1], n_sum)
        
    answer = n_sum    
        
    return answer



# answer = 0

# def dfs(pick, x, n, start, n_sum, sticker):
#     global answer

#     if x==n:
#         answer = max(answer, n_sum)
#         return
    
#     # 이전 스티커를 뜯은 경우
#     if pick:
#         dfs(False, x+1, n, start, n_sum, sticker) 
#     # 이전 스티커를 뜯지 않은 경우
#     else:
#         dfs(False, x+1, n, start, n_sum, sticker)
        
#         if not (x== n-1 and start):
#             dfs(True, x+1, n, start, n_sum+sticker[x], sticker)
    

# def solution(sticker):
#     global answer
    
#     n = len(sticker)
#     dfs(True, 1, n, True, sticker[0], sticker)
#     dfs(False, 1, n, False, 0, sticker)

#     return answer