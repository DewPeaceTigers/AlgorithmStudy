'''
서로 교차하지 않게 하려면 연속적으로 증가하는 숫자가 필요.
가장 긴 증가하는 부분 수열의 길이가 최대로 겹치지 않고 연결'

첫번째 전봇대를 기준으로 오름 차순 정렬
첫번째 전봇대와 연결되어 있는 두번째 전봇대의 수를 최장 증가 수열로 구해주면 
연결될 수 있는 최대 전깃줄 수가 나옴
정답은 N-최대 전깃줄의 수

최장증가수열 : 증가하는 순서대로 숫자를 고르면서 고른 부분 수열의 길이가 최대 길이
'''
n=int(input())

connect = []
for i in range(n) :
    connect.append(list(map(int, input().split())))

connect.sort()
dp=[1]*n
for i in range(n) :
    for j in range(i) :
        if connect[i][1]>connect[j][1] and dp[i]<dp[j]+1:
            dp[i]=dp[j]+1

print(n-max(dp))