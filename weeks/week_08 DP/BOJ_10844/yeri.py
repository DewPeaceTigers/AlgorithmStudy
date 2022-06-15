# ## 못품
# import sys
# input = sys.stdin.readline

# n = int(input())

# one_n_eight=[2,3]
# stair_nums=[9,17]
# for i in range(2,n):
#     stair_nums.append(stair_nums[i-1]*2-one_n_eight[i-2])
#     one_n_eight.append(one_n_eight[i-2]*2)

# print(stair_nums[n-1]%1000000000)
# print(one_n_eight)

## 풀이
import sys
input = sys.stdin.readline

n = int(input())
dp=[[0]*10 for i in range(n+1)]
for i in range(10): dp[1][i]=1
print(dp)

def num(n, d) :
    print(n,d)
    if n==1 : return dp[n][d]
    if dp[n][d]==0:
        if d==0 :
            dp[n][d]=num(n-1, d+1)
        elif d==9 :
            dp[n][d]=num(n-1, d-1)
        else :
            dp[n][d]=num(n-1, d-1)+num(n-1, d+1)
    return dp[n][d] % 1000000000

cnt=0
for i in range(1,10): cnt+=num(n,i)
print(cnt % 1000000000)