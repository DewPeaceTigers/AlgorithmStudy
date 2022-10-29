'''
↑ 는 ←(1은 2)
← 는 ↓(2는 3)
↓ 는 →(3은 0)
→ 는 ↑(0은 1)
=> 방향 1 증가 (dir+1)%4
'''
import sys
input=sys.stdin.readline

n=int(input())

boards=[[0]*101 for _ in range(101)]

dx=[1, 0, -1, 0] #0: →, 1: ↑, 2: ←, 3: ↓
dy=[0, -1, 0, 1]

for _ in range(n) :
    x, y, d, g=map(int, input().split())
    boards[x][y]=1

    moves=[]
    moves.append(d)

    for _ in range(g) :
        for i in range(len(moves)-1, -1, -1) : #거꾸로 꺼내서 방향 전환
            moves.append((moves[i]+1)%4)

    for move in moves:
        nx, ny=x+dx[move], y+dy[move]
        boards[nx][ny]=1
        x, y=nx, ny

ans=0
for i in range(100):
    for j in range(100):
        if(boards[i][j+1]==1 and boards[i+1][j+1]==1 and boards[i+1][j]==1 and boards[i][j]==1) :
            ans+=1

print(ans)
