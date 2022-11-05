import sys
from bisect import bisect_left
input=sys.stdin.readline

n=int(input())
port=list(map(int, input().split()))
dp=[1]
arr=[port[0]]

for i in range(1, n):
    if port[i]>arr[-1]:
        arr.append(port[i])
        dp.append(dp[-1]+1)
    else:
        idx=bisect_left(arr, port[i])
        arr[idx]=port[i]

print(max(dp))
'''
#시간초과
dp=[1]*n
for i in range(1, n) :
    for j in range(i) :
        if port[i]>port[j] :
            dp[i]=max(dp[j]+1, dp[i])

result=max(dp)
print(n-result)
'''