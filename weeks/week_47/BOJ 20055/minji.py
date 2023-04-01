import sys
from collections import deque

input=sys.stdin.readline

n, k=map(int, input().split())
belts=deque(list(map(int, input().split())))
robots=deque([0]*n*2) #로봇 위치
ans=0
while True :
    # 벨트 한칸 회전
    belts.rotate(1)
    robots.rotate(1)
    #robots[n-1]=0 #로봇 내림
    for i in range(n-2, -1, -1) : #로봇 한칸 이동
        if robots[i]==1 and robots[i+1]==0 and belts[i+1]>0 :
            robots[i+1]=1
            robots[i]=0
            belts[i+1]-=1
    robots[n-1]=0 #내리는 위치

    if belts[0]>0 and robots[0]==0 : #올리는 위치
        robots[0]=1
        belts[0]-=1

    ans += 1
    if belts.count(0)>=k :
        break

print(ans)