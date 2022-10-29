'''
n까지
3x2 쓰는 경우 dp[i-2]*3
3X4 쓰는 경우 dp[i-4]*2
3X6 쓰는 경우 dp[i-6]*2
...
3XN 쓰는 경우 2가지
'''
n=int(input())

dp=[0]*31
dp[2]=3


for i in range(4, n+1, 2) :#홀수인 경우는 0
    #dp[i-2]*dp[2] 3x2가 뒤에 오는 경우
    dp[i]=dp[i-2]*3+sum(dp[:i-2])*2+2

print(dp[n])




