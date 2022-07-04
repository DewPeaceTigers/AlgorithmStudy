n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
chess = [[[] for _ in range(n)] for _ in range(n)]
# 동 - 서 - 북 - 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
horse = []

for i in range(k):
    x, y, d = map(int, input().split())
    horse.append([x-1, y-1, d-1])
    chess[x-1][y-1].append(i)

count = 0

def change_dir(d):
    if d in [0, 2]:
        d += 1
    elif d in [1, 3]:
        d -= 1
    return d

def solve(h_num):
    x, y, d = horse[h_num]
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 > nx or nx >= n or 0 > ny or ny >= n or board[nx][ny] == 2:
        d = change_dir(d)
        horse[h_num][2] = d
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 > nx or nx >= n or 0 > ny or ny >= n or board[nx][ny] == 2:
            return True

    horse_up = []
    for h_idx, h_n in enumerate(chess[x][y]):
        if h_n == h_num:
            horse_up.extend(chess[x][y][h_idx:])
            chess[x][y] = chess[x][y][:h_idx]
            break

    if board[nx][ny] == 1:
        horse_up = horse_up[-1::-1]

    for h in horse_up:
        horse[h][0], horse[h][1] = nx, ny
        chess[nx][ny].append(h)

    if len(chess[nx][ny]) >= 4:
        return False
    return True

while True:
    what = False
    if count > 1000:
        print(-1)
        break
    for i in range(k):
        if solve(i) == False:
            what = True
            break
    count += 1
    if what:
        print(count)
        break
    
n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
chess_map = [[[] for _ in range(n)] for _ in range(n)]
chess = [0 for _ in range(k)]

for i in range(k):
    x, y, z = map(int, input().split())
    chess_map[x-1][y-1].append(i)
    chess[i] = [x-1, y-1, z-1]

cnt = 1
while cnt <= 1000:
    for i in range(k):
        flag = move(i)
        if flag:
            print(cnt)
            sys.exit()
    cnt += 1
print(-1)
