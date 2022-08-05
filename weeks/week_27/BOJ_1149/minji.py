import sys

N=int(input())
cost=[]
for i in range(N):
    cost.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, len(cost)) :
    cost[i][0]=min(cost[i-1][1], cost[i-1][2])+cost[i][0]
    cost[i][1]=min(cost[i-1][0], cost[i-1][2])+cost[i][1]
    cost[i][2]=min(cost[i-1][0],  cost[i-1][1])+cost[i][2]
    
print(min(cost[N-1][0], cost[N-1][1], cost[N-1][2]))