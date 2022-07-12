import sys

input=sys.stdin.readline
n, m, x, y, k=map(int, input())

dx=[1, -1, 0, 0]
dy=[0, 0, -1, 1]
dice=[0, 0, 0, 0, 0, 0]
maps=[]
for _ in range(n) :
    maps.append(list(map(int, input().split())))
    
moves=list(map(int, input().split()))

def turn_dice(dir) :
    if dir==1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]=dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]
    elif dir==2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]=dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]    
    elif dir==3:
        dice[0], dice[1], dice[2], dice[3]. dice[4], dice[5]=dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]
    elif dir==4 :
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]=dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]        
for move in moves :
    x, y=x+dx[move-1], y+dy[move-1]
    
    if x<0 or x>=n or y<0 or y>=m :
        x, y=x-dx[move-1], y-dy[move-1]
        continue
    
    turn_dice(move)
    if maps[x][y]==0 :
        maps[x][y]=dice[-1]
    else:
        dice[-1]=maps[x][y]
        maps[x][y]=0
        
    print(dice[0])