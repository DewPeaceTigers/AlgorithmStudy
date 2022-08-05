n=int(input())

open1, open2=map(int, input().split())
m=int(input())
orders=[]
for _ in range(m) :
    orders.append(int(input()))

def solve(orderIdx, open1, open2):
    if orderIdx == M:
        return 0

    if dp[orderIdx][open1][open2] != -1:
        return dp[orderIdx][open1][open2]

    open1_cnt = solve(orderIdx+1, order[orderIdx], open2) + abs(order[orderIdx] - open1)
    open2_cnt = solve(orderIdx+1, open1, order[orderIdx]) + abs(order[orderIdx] - open2)

    dp[orderIdx][open1][open2] = min(open1_cnt, open2_cnt)

    return dp[orderIdx][open1][open2]
    
dp=[[[-1]*(n+1) for _ in range(n)] for _ in range(m)]

print(solve(0, open1, open2))