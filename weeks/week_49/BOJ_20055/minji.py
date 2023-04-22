import sys
from collections import deque

input=sys.stdin.readline
n, k=map(int, input().split())
belts=deque(list(map(int, input().split())))
robots=deque([0]*n*2)
cnt=0

while True:
    #과정 1 벨크와 로봇 한 칸 회전
    belts.rotate(1)
    robots.rotate(1)

    #과정2 내리는 위치 로봇 내리기
    robots[n-1]=0

    #과정3 로봇 한칸 이동
    for i in range(n-2, -1, -1) :
        if robots[i+1]==0 and robots[i]==1 and belts[i+1]>0 :
            belts[i+1]-=1
            robots[i+1]=1
            robots[i]=0

    robots[n-1]=0 #로봇 내리기
    #로봇 올리기
    if robots[0]==0 and belts[0]>0 :
        robots[0]=1
        belts[0]-=1
    cnt+=1
    #종료
    if belts.count(0)>=k :
        break
print(cnt)