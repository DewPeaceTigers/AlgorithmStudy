'''
cost[i][0] : 빨강
cost[i][1] : 초록
cost[i][2] : 파랑

'''
import sys

N=int(input())
cost=[]
for i in range(N):
    cost.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, len(cost)) :
    cost[i][0]=min(cost[i-1][1], cost[i-1][2])+cost[i][0] #i번째집을 빨강으로 칠했을 때
    cost[i][1]=min(cost[i-1][0], cost[i-1][2])+cost[i][1] #초록으로 칠했을 때
    cost[i][2]=min(cost[i-1][0],  cost[i-1][1])+cost[i][2] #파랑으로 칠했을 때

print(min(cost[N-1][0], cost[N-1][1], cost[N-1][2])) #빨강, 초록, 파랑으로 칠했을 때 최솟값 출력