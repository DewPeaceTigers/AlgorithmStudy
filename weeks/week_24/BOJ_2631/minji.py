#-*- coding: utf-8 -*-
'''
LIS �˰��� �̿�
LIS�� �����ְ� ������ ���ڵ��� ���ڸ��� �������ָ� ��
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
