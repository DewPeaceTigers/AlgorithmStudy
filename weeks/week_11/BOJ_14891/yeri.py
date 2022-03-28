"""
구현했다.
"""
import sys
input = sys.stdin.readline

# 1: 3 / 2: 7, 3 / 3: 7, 3 / 4: 7
gears=[list(input().strip()) for _ in range(4)]
n = int(input())
moves=[list(map(int,input().split())) for _ in range(n)]

meets=[[2],[6,2],[6,2],[6]]

for i in range(n):
    target, dir = moves[i]
    shouldMove=[False]*3
    movements=[0]*4
    for m in range(3):
        if gears[m][meets[m][-1]]!=gears[m+1][meets[m+1][0]]: shouldMove[m]=True

    movements[target-1]=dir
    for i in range(target,4):
        if shouldMove[i-1] : movements[i]=-movements[i-1]
    for i in range(target-2,-1,-1):
        if shouldMove[i]: movements[i]=-movements[i+1]
    for i, movement in enumerate(movements):
        if movement==0 : continue
        cnt=0
        idx=0
        temp = gears[i][idx]
        while cnt!=8:
            cnt+=1
            b_temp = temp
            idx = 7 if (idx+movement)==-1 else (idx+movement)%8
            temp = gears[i][idx]
            gears[i][idx]=b_temp
print(sum([ 2**i if gears[i][0]=='1' else 0 for i in range(4)]))