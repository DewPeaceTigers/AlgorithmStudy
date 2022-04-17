import sys
input=sys.stdin.readline

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1] # 북동남서
n, m=map(int, input().split())
x, y, dir=map(int, input().split()) #0: 북, 1: 동, 2: 남, 3: 서
boards=[]
visit=[[0] * m for _ in range(n)]

for i in range(n) :
    boards.append(list(map(int, input().split())))

visit[x][y]=1
count=1 #청소하는 칸
exit_count=0 #종료 조건 카운트
while 1:
    dir=(dir-1)%4 #회전
    nx, ny=x+dx[dir], y+dy[dir]
    if visit[nx][ny]==0 and boards[nx][ny]==0 :
        x, y=nx, ny
        visit[nx][ny]=1
        count+=1
        exit_count=0
        continue
    else:
        exit_count+=1
    if exit_count==4 :
        nx, ny= x-dx[dir], y-dy[dir] #뒤가 벽인지 확인
        if boards[nx][ny]==1 :
            break
        else:
            x, y=nx, ny
        exit_count=0

print(count)
