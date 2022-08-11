import sys
from collections import deque

input = sys.stdin.readline

n,Q = map(int,input().split())
N = pow(2,n)
boards=[list(map(int,input().split())) for _ in range(N)]
iced = [[0]*N for _ in range(N)]
level = list(map(int,input().split()))

dr = [-1,0,+1,0]
dc = [0,-1,0,+1]

sum = 0
max_count = 0
for idx, l in enumerate(level):
    L = pow(2,l)
    for i in range(0,N,L):
        for j in range(0,N,L):
            temp = [ boards[i+il][j:j+L] for il in range(L) ]
            for xl in range(L):
                for yl in range(L):
                    boards[i+yl][j+L-1-xl] = temp[xl][yl]

    temp = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if boards[i][j]==0: continue
            cnt=0
            for d in range(4):
                nr = i+dr[d]
                nc = j+dc[d]
                if not(-1<nr<N and -1<nc<N): continue
                if boards[nr][nc]!=0: cnt+=1
            temp[i][j]=boards[i][j]
            if cnt<3 : temp[i][j]-=1
    for i in range(N): boards[i] = temp[i][:]

    if idx==Q-1:
        visited=[[False]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                sum+=boards[i][j]
                if not visited[i][j] and boards[i][j]!=0:
                    q = deque([[i,j]])
                    visited[i][j]=True
                    cnt=1
                    while q:
                        r,c = q.popleft()
                        for d in range(4):
                            nr = r+dr[d]
                            nc = c+dc[d]
                            if not(-1<nr<N and -1<nc<N) or visited[nr][nc] or boards[nr][nc]==0:continue
                            q.append([nr,nc])
                            visited[nr][nc]=True
                            cnt+=1
                    max_count = max(cnt,max_count)
print(sum)
print(max_count)
