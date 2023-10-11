import sys
from collections import deque
input = sys.stdin.readline

N, M, x, y, K  = map(int,input().split())

dx = [0,0,-1,1]
dy = [1,-1,0,0]

boards = [list(map(int,input().split())) for _ in range(N)]

dice = [0]*6
orders = list(map(int,input().split()))

for dir in orders:
    nx = x+dx[dir-1]
    ny = y+dy[dir-1]
    # print('dir',dir, nx,ny)
    if not(-1<nx<N and -1<ny<M):
        continue
    [a,b,c,d,e,f] = dice
    # print(dice,a,b,c,d,e,f)
    if dir == 1:
        # 동쪽
        dice = [c,b,f,a,e,d]
    if dir == 2:
        # 서쪽
        dice = [d,b,a,f,e,c]
    if dir == 3:
        # 북쪽
        dice = [b,f,c,d,a,e]
    if dir == 4:
        # print("north")
        # 남쪽
        dice = [e,a,c,d,f,b]
    # print(dice)
    # print(nx,ny,boards[nx][ny])
    if boards[nx][ny]!=0:
        dice[0] = boards[nx][ny]
        boards[nx][ny] = 0
    else :
        boards[nx][ny] = dice[0]
    # print(dice)
    x, y = nx, ny
    print(dice[5])