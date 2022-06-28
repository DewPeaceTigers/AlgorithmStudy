import sys

input=sys.stdin.readline

n=int(input())
'''
메모리 초과 코드
boards=[]

for _ in range(n) :
    boards.append(list(map(int, input().split())))

max_dp=[[0] * 3 for _ in range(n)]
min_dp=[[0]*3 for _ in range(n)]
    
for i in range(n) :
    max_dp[0][i]=boards[0][i]
    min_dp[0][i]=boards[0][i]
    
for i in range(1, n) :
    for j in range(3) :
        if j==0 :
            max_dp[i][j]=max(max_dp[i-1][0], max_dp[i-1][1])+boards[i][j]
            min_dp[i][j]=min(min_dp[i-1][0], min_dp[i-1][1])+boards[i][j]
        elif j==1 : 
            max_dp[i][j]=max(max_dp[i-1][0], max_dp[i-1][1], max_dp[i-1][2])+boards[i][j]
            min_dp[i][j]=min(min_dp[i-1][0], min_dp[i-1][1], min_dp[i-1][2])+boards[i][j]
        else: 
            max_dp[i][j]=max(max_dp[i-1][2], max_dp[i-1][1])+boards[i][j]
            min_dp[i][j]=min(min_dp[i-1][1], min_dp[i-1][2])+boards[i][j]
            
print(max(max_dp[n-1]), min(min_dp[n-1]))
'''
max_dp=[0]*3
min_dp=[0]*3

max_tmp=[0]*3
min_tmp=[0]*3
for i in range(n) :
    a, b, c=map(int, input().split())
    for j in range(3) :
        if j==0 :
            max_tmp[j]=a+max(max_dp[1], max_dp[0])
            min_tmp[j]=a+min(min_dp[0], min_dp[1])
        elif j==1:
            max_tmp[j]=b+max(max_dp[0], max_dp[1], max_dp[2])
            min_tmp[j]=b+min(min_dp[0], min_dp[1], min_dp[2])
        else:
            max_tmp[j]=c+max(max_dp[1], max_dp[2])
            min_tmp[j]=c+min(min_dp[1], min_dp[2])
    for j in range(3) :
        max_dp[j]=max_tmp[j]
        min_dp[j]=min_tmp[j]
        
print(max(max_dp), min(min_dp))