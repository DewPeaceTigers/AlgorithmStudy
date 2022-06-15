'''
n번째 잔을 마셨을 때
1. n-1잔을 마셨으면 n-2잔은 불가능
2. n-1잔을 안 마셨으면 n-2잔은 가능
3. 현재 잔을 안마시는 경우
점화식
1. dp(n)=dp(n-3)+glass(n-2)+glass(n)
2. dp(n)=dp(n-2)+glass(n)
3. dp(n-1)

이 세 경우 중 가장 큰 값을 저장
'''
import sys

n=int(input())
glass=[]
for i in range(n) :
    glass.append(int(sys.stdin.readline()))

dp=[0]*n

dp[0]=glass[0]
if n>1 :
    dp[1]=glass[0]+glass[1]

if n>2 :
    dp[2]=max(glass[0]+glass[2], glass[1]+glass[2], dp[1])

for i in range(3, n) :
    dp[i]=max(dp[i-1], dp[i-3]+glass[i-1]+glass[i], dp[i-2]+glass[i])

print(dp[n-1])