import sys
from collections import deque,defaultdict
input = sys.stdin.readline

N = int(input())
students = [list(map(int,input().split())) for _ in range(N**2)]
placeList = [[-1,-1]]*(N**2)
boards = [[-1]*N for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]
for student in students:
    n = student[0]
    likes = student[1:]
    cands = defaultdict(int)
    for i in likes:
        if placeList[i-1]==[-1,-1]: continue
        r,c = placeList[i-1]
        for d in range(4):
            nr = r+dx[d]
            nc = c+dy[d]
            if not(-1<nr<N and -1<nc<N): continue
            if boards[nr][nc] == -1:
                cands[(nr,nc)] +=1
    candList = list(cands.items())
    if not candList:
        for i in range(N):
            for j in range(N):
                candList.append([(i,j),0])
    candList.sort(reverse=True, key=lambda x:(x[1],-x[0][0], -x[0][1]))
    max_cand = candList[0]
    max_cnt = max_cand[1]

    vacant_dict = defaultdict(int)
    for (r,c), cnt in candList:
        if boards[r][c] != -1: continue
        vacant_cnt = 0
        if max_cnt > cnt: break
        for d in range(4):
            nr = r+dx[d]
            nc = c+dy[d]
            if not(-1<nr<N and -1<nc<N): continue
            if boards[nr][nc] == -1:
                vacant_cnt+=1
        vacant_dict[(r,c)]=(vacant_cnt)
    vacantList = list(vacant_dict.items())
    bestPos = max(vacantList, key=lambda x:(x[1],-x[0][0], -x[0][1]))
    placeList[n-1] = bestPos[0]
    boards[bestPos[0][0]][bestPos[0][1]] = n

result = 0
students.sort(key=lambda x:x[0])
for x in range(N):
    for y in range(N):
        now = boards[x][y]
        cnt = 0
        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]
            if not(-1<nx<N and -1<ny<N): continue
            if boards[nx][ny] in students[now-1]:
                cnt +=1
        result += 10**(cnt-1) if cnt!=0 else 0
print(result)