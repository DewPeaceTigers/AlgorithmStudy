import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
people=[list(map(int,input().split())) for i in range(n)]
for i in range(n): # 하나씩 다 확인하기 크기가 적어서 가능
    rank=1
    for j in range(n):
        if i!=j:
            if people[i][0]<people[j][0] and people[i][1]<people[j][1]:
                rank+=1
    print(rank,end=" ")