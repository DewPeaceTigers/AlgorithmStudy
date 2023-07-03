import sys

input = sys.stdin.readline

# 세로크기 N, 가로크기 M 입력 (4 ≤ N, M ≤ 500)
N, M = map(int, input().split())

paper = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 방문 체크
visited = [[False]*M for _ in range(N)]

max_sum = 0


def dfs(x, y, cnt, t_sum):
    global max_sum

    if cnt == 4:
        max_sum = max(max_sum, t_sum)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 경계 체크 & 방문 체크
        if nx < 0 or nx >= N or ny < 0 or ny >= M or visited[nx][ny]:
            continue

        visited[nx][ny] = True
        dfs(nx, ny, cnt+1, t_sum + paper[nx][ny])
        visited[nx][ny] = False


# 'ㅜ' 모양 블록 계산
def spBlock(x, y):
    t_sum = paper[x][y]

    cnt = 0
    t_min = 1e9

    for i in range(4):

        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        cnt += 1
        t_sum += paper[nx][ny]
        t_min = min(t_min, paper[nx][ny])

    # 상하좌우 탐색이 모두 성공한 경우는 그 중 최솟값 빼주기
    if cnt == 4:
        return t_sum - t_min
    # 3방향만 성공인 경우는 합 그대로 리턴
    elif cnt == 3:
        return t_sum
    # 모양 만들기 실패한 경우
    else:
        return -1


for r in range(N):
    for c in range(M):
        visited[r][c] = True

        # 'ㅜ' 제외한 나머지 dfs 탐색
        dfs(r, c, 1, paper[r][c])
        # 'ㅜ' 처리
        max_sum = max(max_sum, spBlock(r, c))
        visited[r][c] = False

print(max_sum)
