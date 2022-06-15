import sys
input = sys.stdin.readline

num = list(map(int,list(input().strip())))

dp=[0]*len(num)

for i in range(len(dp)):
    if i==0 and num[i]!=0:
        dp[i]=1
        continue
    if num[i]>0:
        # 10, 20은 무조건 두자리수에서만 가능
        dp[i]+=dp[i-1]
    if num[i-1]==1:
        if(i-2>=0): dp[i]+=dp[i-2]
        else : dp[i]+=1
    elif num[i-1]==2 and num[i]<7:
        if(i-2>=0): dp[i]+=dp[i-2]
        else : dp[i]+=1
print(dp[-1]%1000000)