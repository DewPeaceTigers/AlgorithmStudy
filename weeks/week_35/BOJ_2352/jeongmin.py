import sys
from bisect import bisect

input = sys.stdin.readline

n = int(input())
ports = list(map(int, input().split()))

# 증가하는 가장 긴 수열
dp = [ports[0]]

for i in range(1, n):
    if dp[-1] < ports[i]:
        dp.append(ports[i])
    else:
        dp[bisect(dp, ports[i])] = ports[i]

print(len(dp))