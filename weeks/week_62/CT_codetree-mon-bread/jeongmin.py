from collections import deque

# n : 격자의 크기, m : 사람 수
n, m = map(int, input().split())

# 격자 정보 (0: 빈칸, 1: 베이스캠프, -1:지니갈 수 없는 칸)
board = [list(map(int, input().split())) for _ in range(n)]

# 사람들이 가고자 하는 편의점 위치
store = []
for _ in range(m):
    a, b = list(map(int, input().split()))
    store.append([a-1, b-1])

# 사람들 위치
people = [[] for _ in range(m)]

# 상, 좌, 우, 하
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

INF = 15*15

# 최단 거리 저장
dist = [[INF]*n for _ in range(n)]


def in_range(x, y):
    global n
    return 0 <= x < n and 0 <= y < n


# 시작점부터 갈 수 있는 모든 지점까지의 최단거리 구하기
def bfs(sx, sy):
    global dist

    # 최단거리 배열 초기화
    dist = [[INF]*n for _ in range(n)]

    # (sx, sy) 에서 모든 지점까지의 최단거리 구하기
    q = deque()
    q.append((sx, sy))
    dist[sx][sy] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 경계를 벗어나면 무시
            if not in_range(nx, ny):
                continue

            # 지니갈 수 없는 칸인 경우 무시
            if board[nx][ny] == -1:
                continue

            if dist[x][y]+1 < dist[nx][ny]:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))


def move_person(idx):  # 사람 이동
    global people, n

    x, y = people[idx]

    # 이미 편의점에 도착한 경우 무시
    if is_arrive(idx):
        return

    # 사람이 가고자하는 편의점에서 모든 위치까지의 최단거리 계산
    bfs(store[idx][0], store[idx][1])

    min_dist, min_x, min_y = INF, -1, -1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 경계벗어남
        if not in_range(nx, ny):
            continue

        # 지나갈 수 없는 칸
        if board[nx][ny] == -1:
            continue

        if dist[nx][ny] < min_dist:
            min_dist = dist[nx][ny]
            min_x, min_y = nx, ny

    # 사람 이동
    people[idx] = [min_x, min_y]


def is_arrive(idx):  # 사람이 편의점에 도착했는지
    return people[idx] == store[idx]


def update(idx):
    x, y = people[idx]
    if is_arrive(idx) and board[x][y] != -1:
        board[x][y] = -1


# 베이스캠프에서 출발
def enter_basecamp(idx):
    global n, people

    # idx번 사람이 가고자 하는 편의점에서 가장 가까운 베이스캠프 찾기
    bfs(store[idx][0], store[idx][1])

    min_dist, min_x, min_y = INF, -1, -1
    for x in range(n):
        for y in range(n):
            if board[x][y] == 1:
                if dist[x][y] < min_dist:
                    min_dist = dist[x][y]
                    min_x = x
                    min_y = y

    # idx 번 사람 베이스캠프에서 출발
    people[idx] = [min_x, min_y]
    # 베이스캠프 지나갈 수 없는 칸으로 처리
    board[min_x][min_y] = -1


def is_finish():  # 모든 사람이 편의점에 도착했는지
    global n

    for i in range(m):
        if not is_arrive(i):
            return False
    return True


t = 0
while True:
    t += 1

    # 격자에 있는 사람 모두 이동
    for i in range(min(t-1, m)):
        move_person(i)

    # 편의점 도착한 경우 지나갈 수 없는 칸으로 처리
    for i in range(min(t-1, m)):
        update(i)

    if t <= m:
        enter_basecamp(t-1)

    if t > m and is_finish():
        break

print(t)
