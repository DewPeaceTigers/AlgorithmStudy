import sys
input = sys.stdin.readline

N = int(input())

max_dp=[0]*3
min_dp=[0]*3
max_temp = [0]*3
min_temp = [0]*3
for i in range(N):
    nums=list(map(int,input().split())) # 이걸 안해서 메모리 초과가 계속 났다
    for j in range(3):
        # 지금 j가 가질 수 있는 가장 큰 수와 작은 수
        if j==0:
            min_temp[j] = min(min_dp[0],min_dp[1])+nums[j]
            max_temp[j] = max(max_dp[0],max_dp[1])+nums[j]
        elif j ==1:
            min_temp[j] = min(min_dp[0],min_dp[1],min_dp[2])+nums[j]
            max_temp[j] = max(max_dp[0],max_dp[1],max_dp[2])+nums[j]
        else:
            min_temp[j] = min(min_dp[1],min_dp[2])+nums[j]
            max_temp[j] = max(max_dp[1],max_dp[2])+nums[j]
    max_dp = max_temp[:]
    min_dp = min_temp[:]
print(max(max_dp),min(min_dp))