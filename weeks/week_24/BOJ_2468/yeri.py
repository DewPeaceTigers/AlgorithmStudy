import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

spaces = [ list(map(int,input().split())) for _ in range(n)]

heights = sorted(list(set(sum(spaces,[]))))
dx=[-1,+1,0,0]
dy=[0,0,-1,+1]

area=1
for height in heights:
    visit = [[False]*n for _ in range(n)]
    area_count=0

    for i in range(n):
        for j in range(n):
            if spaces[i][j] > height and not visit[i][j]:
                area_count+=1
                # 안잠긴 영역을 기점으로 체크
                q= deque([(i,j)])
                visit[i][j]=True
                while q:
                    x,y = q.popleft()
                    for d in range(4):
                        nx = x+dx[d]
                        ny = y+dy[d]
                        if not (-1<nx<n and -1<ny<n): continue
                        if not visit[nx][ny] and spaces[nx][ny] > height:
                            q.append((nx,ny))
                            visit[nx][ny]=True
    area = max(area, area_count)
print(area)