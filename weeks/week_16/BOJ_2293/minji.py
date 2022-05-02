'''
못품
dp[i]->i원을 만들 때 가능한 경우의 수
dp[0]->동전 하나만 사용
'''
n, k=map(int, input().split())
costs=[]
for i in range(n) :
    costs.append(int(input()))
dp=[0]*(k+1)
dp[0]=1

for cost in costs:
    for i in range(cost, k+1) :
        #cost로 i원을 만드는 방법의 수
        count=dp[i-cost]
        dp[i]+=count

print(dp[k])