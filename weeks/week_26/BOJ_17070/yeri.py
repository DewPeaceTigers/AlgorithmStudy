def dfs(pos):
    global cnt
    x, y, z = pos

    # n,n 도달
    if x == n - 1 and y == n - 1:
        cnt += 1
        return

    # 가로 세로 대각선의 경우 대각선 이동
    if x + 1 < n and y + 1 < n:
        if graph[x + 1][y + 1] == 0 and graph[x][y + 1] == 0 and graph[x + 1][y] == 0:
            dfs((x + 1, y + 1, 2))

    # 가로 대각선의 경우 가로 이동
    if z == 0 or z == 2:
        if y + 1 < n:
            if graph[x][y + 1] == 0:
                dfs((x, y + 1, 0))

    # 세로 대각선의 경우 세로 이동
    if z == 1 or z == 2:
        if x + 1 < n:
            if graph[x + 1][y] == 0:
                dfs((x + 1, y, 1))


n = int(input())
graph = [[] for _ in range(n)]
cnt = 0
# 그래프 정보 입력
for i in range(n):
    graph[i] = list(map(int, input().split()))

# x,y,현재방향
dfs((0, 1, 0))

print(cnt)