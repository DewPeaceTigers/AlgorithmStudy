# 하나의 토마토에 인접한 곳 : 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향
# 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수
from collections import deque

# 가로, 세로, 높이
N, M, H = map(int, input().split())

# 상자에 저장된 토마토들의 정보 주어짐
# 1: 익은 토마토, 0: 익지 않은 토마토, -1: 토마토가 들어있지 않은 칸
box = [[list(map(int, input().split())) for _ in range(M)] for _ in range(H)]

# 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 0, 0, -1, 1]
dz = [0, 0, -1, 1, 0, 0]

ripe = []
not_ripe = 0    # 익지 않은 토마토 개수
ans = 1

def check(box):
    # 토마토가 모두 익지 못하는 상황이면
    for i in range(H):
        for j in range(M):
            for k in range(N):
                if box[i][j][k] == 0:
                    return False
    return True

def bfs(ripe, box, N, M, H):
    global ans, not_ripe
    # bfs를 수행하는 순서가 중요..
    # 처음 토마토가 있는 위치부터 시작할 수 있도록
    # 익은 토마토 위치를 저장한 리스트를 큐에 먼저 저장
    q = deque(ripe)

    while q:
        x, y, z = q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            # 범위 확인
            if 0<=nx<H and 0<=ny<M and 0<=nz<N:
                if box[nx][ny][nz] == 0:
                    not_ripe -= 1  # 익지 않은 토마토 개수 감소시키기
                    box[nx][ny][nz] = box[x][y][z]+1
                    q.append((nx, ny, nz))
                    ans = max(ans, box[nx][ny][nz])

# print(box)

for i in range(H):
    for j in range(M):
        for k in range(N):
            if box[i][j][k] == 1:
                ripe.append((i, j, k))
                # bfs(i, j, k, box, N, M, H)
            elif box[i][j][k] == 0:
                not_ripe +=1

bfs(ripe, box, N, M, H)

if not_ripe > 0:    # 익지 않은 토마토가 남은 경우
    print(-1)
else:
    print(ans-1)