"""
최장 증가 수열
- dp를 이용한 방법 > 시간 초과
- binary search를 이용해서 구하기!!
"""

import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

res = []

for num in arr:
    if not res or res[-1] < num:
        res.append(num)
        continue
    else:
        idx = bisect_left(res, num)
        res[idx] = num

print(n-len(res))