from collections import deque
import sys 

input = sys.stdin.readline 

# 세로, 가로 크기 입력
R, C = map(int, input().split())

# 보물 지도 정보 입력 : 육지(L), 바다(W)
treasure = [list(input().rstrip()) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def island(a, b, r, c):
    dist = [[-1]*c for i in range(r)]

    # 가장 긴 시간이 걸리는 육지
    maxDist = 0

    q = deque([[a, b]])
    dist[a][b] = 0
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=r or ny<0 or ny>=c:
                continue

            if dist[nx][ny] == -1 and treasure[nx][ny] == 'L':
                dist[nx][ny] = dist[x][y] + 1

                maxDist = max(maxDist, dist[nx][ny])
                q.append([nx, ny])
    # print(a, b)
    # for i in range(r):
    #     print(*dist[i])        
    return maxDist


result = 0
for i in range(R):
    for j in range(C):
        # 육지인 경우 이동 거리 확인
        if treasure[i][j] == 'L':
            result = max(result, island(i, j, R, C))

print(result)