"""풀이 찾아봄.. [dfs + DP]"""
import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

N, M = map(int, input().split())
mmap = [list(map(int, input().split())) for _ in range(N)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 임의의 점(a, b)에서 도착지점 (m-1, n-1) 까지 가는 경우의 수 구하기
path = [[-1]*M for _ in range(N)]


def dfs(x, y):
    global N, M

    # 제일 오른쪽 아래 지점에 도착한 경우 1을 리턴
    if x == N-1 and y == M-1:
        return 1

    # 이미 방문한 적이 있다면 그 위치에서 출발하는 경우의 수를 리턴
    if path[x][y] != -1:
        return path[x][y]

    path[x][y] = 0
    # 상, 하, 좌, 우 이동
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        # 범위 체크
        if nx < 0 or N <= nx or ny < 0 or M <= ny:
            continue

        # 높이가 낮은 경우에만 이동
        if mmap[nx][ny] < mmap[x][y]:
            path[x][y] += dfs(nx, ny)

    return path[x][y]


print(dfs(0, 0))    # 제일 왼쪽 위 지점에서 출발