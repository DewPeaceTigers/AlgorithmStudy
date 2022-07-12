#-*- coding: utf-8 -*-
'''
LIS 알고리즘 이용
LIS로 구해주고 나머지 숫자들을 제자리로 정렬해주면 됨
'''
n=int(input())

kids=[int(input()) for _ in range(n)]
dp=[0]*n

dp[0]=1
for i in range(1, n) :
    dp[i]=1
    for j in range(i) :
        if kids[i]>kids[j] :
            dp[i]=max(dp[i], dp[j]+1)
            
print(n-max(dp))
