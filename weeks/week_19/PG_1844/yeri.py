from collections import deque
def solution(maps):
    q=deque([[1,0,0]])
    dx=[-1,0,+1,0]
    dy=[0,-1,0,+1]
    maps[0][0]=0
    while q:
        time,x,y = q.popleft()
        if x==len(maps)-1 and y==len(maps[0])-1:
            return time
        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]
            if -1<nx<len(maps) and -1<ny<len(maps[0]) and maps[nx][ny]==1:
                q.append([time+1,nx,ny])
                maps[nx][ny]=0
    return -1