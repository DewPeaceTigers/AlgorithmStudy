import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
K = int(input())

boards = [[False]*N for _ in range(N)]
for _ in range(K):
    x,y = map(int,input().split())
    boards[x-1][y-1] = True
    
snakes =[[False]*N for _ in range(N)]
snakes[0][0] = True

L = int(input())
directs = [input().split() for _ in range(L)]

dr = [0,1,0,-1] # 동, 남, 서, 북
dc = [1,0,-1,0]
sd = 0 # 처음에 오른쪽을 향한다
time = 0
snake = deque([[0,0]])

now = 0
while True:
    time+=1
    if now<len(directs):X, C = directs[now]
    fr,fc = snake[0]
    fr += dr[sd]
    fc += dc[sd]
    if not(-1<fr<N and -1<fc<N) or snakes[fr][fc]: break
    if boards[fr][fc] :
        boards[fr][fc] = False
    else:
        pr,pc = snake.pop() # 꼬리 삭제
        snakes[pr][pc] = False
    snakes[fr][fc] = True
    snake.appendleft([fr,fc])
    if now <len(directs) and time == int(X):
        if C == 'L': sd = (sd-1) if sd-1!=-1 else 3
        if C == 'D': sd = (sd+1)%4
        now +=1
print(time)
