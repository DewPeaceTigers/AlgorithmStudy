import sys
input = sys.stdin.readline

a = list(input().strip())
b = list(input().strip())

dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]

for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if a[i-1]==b[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else : dp[i][j] = max(dp[i][j-1],dp[i-1][j])

print(dp[-1][-1])

"""
내가 구해야 하는 것 : 두 문자열 사이의 LCS 길이
각 원소 : 행에서 현재까지 나온 문자열과 열에서 나온 문자열 사이의 LCS 길이
ACAY & CA 이 두개를 비교하여 나오는 LCS 값이 원소

같다면
현재 = 공통 요소인 현재 위치에서 이 글자를 추가하기 전의 LCS + 1
다르다면
현재 = A를 추가하거나 B를 추가해서 나오는 LCS 즉, 왼쪽이나 위쪽 중 큰 LCS +1
"""