import sys

input = sys.stdin.readline

code = ['9'] + list(input().rstrip())

# (암호 길이 +1) 저장
l = len(code)

# 해석 가능한 가짓수 저장
dp = [0] * l

# 초기값 설정
dp[0] = 1

for i in range(1, l):
    # 암호 첫 번째 자리가 0인 경우 해석 불가능
    if code[1] == '0':
        break

    # 한 자리 암호 해석 ( 1~9 가능)
    if code[i] != '0':
        dp[i] = dp[i-1] % 1000000

    # 두 자리 암호 해석 (앞에 나온 숫자랑 합해서 알파벳을 만들 수 있는 경우)
    if code[i-1] != '0' and 1 <= int(code[i-1]+code[i]) <= 26:
        dp[i] += dp[i-2] % 1000000

print(dp[l-1] % 1000000)

"""
[반례]
121074110
정답: 2
"""