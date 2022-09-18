import sys
import bisect

input = sys.stdin.readline

N = int(input())
els = list(map(int,input().split()))

dp = [els[0]]

for i in range(N):
    if els[i] > dp[-1]:
        # 현재 i가 이전 위치 보다 크면 dp에 추가
        dp.append(els[i])
    else:
        # 작거나 같으면 이전 위치 원소 중 가장 큰 원소의 index 구하기
        idx = bisect.bisect_left(dp,els[i])
        dp[idx] = els[i]
print(len(els)-len(dp))