'''
dp[i]는 입력받은 암호중 i까지 만드는 경우의 수
i번째 경우의 수를 구할때
(i-2)*10+(i-1)이 10 이상 26이하일 때는 dp[i-2]+dp[i-1]
아닐 때는 dp[i-1]
'''
cypher=list(map(int, input()))
l=len(cypher)
dp=[0]*(l+1)
if cypher[0]==0:
    print("0")
else:
    dp[0]=1
    dp[1]=1
    for i in range(2, l+1):
        if cypher[i-1]>0:
            dp[i]+=dp[i-1]
        if 10<=cypher[i-2]*10+cypher[i-1]<=26:
            dp[i]+=dp[i-2]
        dp[i]%=1000000
    print(dp[l])


