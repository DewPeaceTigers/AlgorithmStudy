from collections import deque

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

n, m=12, 6

maps=[list(map(str, input().rstrip())) for _ in range(n)]
ans=0

def pop(tmp) : #삭제
    for a, b in tmp:
        maps[a][b]='.'

def down() : #아래로 당기는 함수
    for i in range(m) :
        for j in range(n-2, -1, -1) :
            for k in range(n-1, j, -1) :
                if maps[k][i] == "." and maps[j][i] !="." :
                    maps[k][i]=maps[j][i]
                    maps[j][i]="."
                    break

def bfs(a, b) : #4개 확인
    q=deque()
    q.append([a, b])
    tmp.append([a, b])
    while q :
        x, y=q.popleft()
        for i in range(4) :
            nx, ny=x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m :
                if maps[nx][ny]==maps[x][y] and visit[nx][ny]==False:
                    q.append([nx, ny])
                    tmp.append([nx, ny])
                    visit[nx][ny]=True

while True :
    flag=0
    visit=[[False]*m for _ in range(n)]
    for i in range(n) :
        for j in range(m) :
            if maps[i][j]!='.' and visit[i][j]==False :
                visit[i][j]=1
                tmp=[] #4개 위치
                bfs(i, j)

                if len(tmp)>=4 :
                    flag=1
                    pop(tmp)

    if flag==0 : break
    down()
    ans+=1
print(ans)