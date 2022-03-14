'''
점화식
세개의 계단을 연달아서 올라갈 수 없으므로
n번째 계단을 오를 때 
1. n-2까지 올라오고 n번째를 오르는 경우
2. n-3까지 올라오고 n-1, n을 오르는 경우

오류
dp[0], dp[1], dp[2] 초기값을 설정할 때 조건을 안달아주면 오류
'''
N=int(input())
dp=[0]*(N+1)
stair=[0]*(N+1)
for i in range(N):
    stair[i]=int(input())
if N>0:
    dp[0]=stair[0]
if N>1:
    dp[1]=stair[0]+stair[1]
if N>2:
    dp[2]=max(stair[1]+stair[2], stair[0]+stair[2])
for i in range(3, N):
    dp[i]=max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i])

print(dp[N-1])