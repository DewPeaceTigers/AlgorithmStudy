"""
DP 활용

[내풀이]
1. 그냥 출력          
    dp[i-1]+1
2. 복사 & 붙여넣기 활용 (붙여넣기 버튼을 여러번 누르는 모든 경우 확인해보기)
    dp[i-3]*2 : Ctrl-A + Ctrl-C + Ctrl-V 
    dp[i-4]*3 : Ctrl-A + Ctrl-C + Ctrl-V + Ctrl-V 
    dp[i-5]*4 : Ctrl-A + Ctrl-C + Ctrl-V + Ctrl-V + Ctrl-V  
    ...
    dp[i-i]*(i-1)

[다른풀이]
https://blog.naver.com/mym0404/222323009491
- 위의 블로그를 참고하면 붙여넣기를 4번이상 안해도 된다고 한다!
"""

import sys

input = sys.stdin.readline

N = int(input())

# dp[i]: 버튼을 i번 눌러 화면에 출력할 수 있는 A개수의 최댓값
dp = [i+1 for i in range(N)]

# N이 6이하인 경우는 그냥 출력이 최댓값이므로 7이상부터 계산
for i in range(6, N):
    # # 복사 & 붙여넣기를 활용하는 모든 경우 확인해보기
    # for j in range(3, i+1):
    #     dp[i] = max(dp[i], dp[i-j]*(j-1))

    # ===== 찾아본 풀이 =====
    # 붙여넣기를 4번까지만 해보면 됨!
    dp[i] = max(dp[i], dp[i-3]*2, dp[i-4]*3, dp[i-5]*4)

print(dp[N-1])
