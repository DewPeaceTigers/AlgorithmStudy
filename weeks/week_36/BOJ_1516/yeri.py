import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
buildings = []
for i in range(N):
    temp = list(map(int,input().split()))
    buildings.append([temp[0],sorted(temp[1:-1]) if len(temp)!=2 else [],i])
sorted_b= deque(sorted(buildings,key=lambda x:(len(x[1]),x[0])))
dp = [0]*N
while sorted_b:
    time, forward, idx = sorted_b.popleft()
    isConstruct = True
    if not forward:
        dp[idx] = time
    else:
        for_time = 0
        for f in forward:
            if dp[f-1]!=0:
                for_time = max(dp[f-1],for_time)
            else:
                isConstruct = False
                break
        if isConstruct :dp[idx] = max([ dp[f-1] for f in forward])+time
    if not isConstruct:
        sorted_b.append([time,forward,idx])
print(dp)
