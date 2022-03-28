'''
그리디
서류 성적을 기준으로 정렬
면접 서류 성적이 높으면 제외
'''
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    newones=[list(map(int,input().split())) for _ in range(N)]
    newones.sort()
    dp=[[]]*N
    dp[0]=[newones[0]]
    for i in range(1,N):
        dp[i] = dp[i-1]
        if dp[i-1][-1][1] > newones[i][1]:
            dp[i].append(newones[i])
        # else: # 왜 이걸 넣으면 틀릴까?
        #     if len(dp[i-1])==1:
        #         dp[i]=[newones[i]]
    print(len(dp[N-1]))
