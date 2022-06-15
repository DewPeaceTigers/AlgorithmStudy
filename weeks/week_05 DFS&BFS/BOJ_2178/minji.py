from collections import deque

n, m = map(int, input().split())
board=[]
for i in range(n) :
    board.append(list(map(int, input())))
visited=[]
count=0
def bfs(x, y) :
    global count
    dx=[-1, 1, 0, 0] #상하좌우 이동
    dy=[0, 0, -1, 1]
    queue=deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4) :
            nx=x+dx[i] #x 이동
            ny=y+dy[i] #y 이동

            if nx<0 or nx >=n or ny < 0 or ny >=m : #범위 박으로 나간 경우
                continue

            if board[nx][ny] == 0 : #0이면 이동 불가
                continue
            if board[nx][ny] == 1 : #1이면 이동 가능
                board[nx][ny]=board[x][y]+1 #몇번 이동했는지 count
                queue.append((nx, ny)) #이동한 곳 좌표 큐에 삽입
    return board[n-1][m-1]
print(bfs(0, 0))