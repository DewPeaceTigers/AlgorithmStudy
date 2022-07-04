import sys

input = sys.stdin.readline

# 체스판의 크기, 말의 개수
N, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]     # 체스판 색 정보
pieces = [[] for i in range(K)]     # 이동할 말의 좌표, 방향 저장

info = [[[] for _ in range(N)] for _ in range(N)]   # 체스판 말 정보
for i in range(K):
    x, y, d = map(int, input().split())
    if not info[x-1][y-1]:
        pieces[i] = [x-1, y-1, d%4]
    info[x-1][y-1].append([i + 1, d%4])

# 하(4), 우(1), 좌(2), 상(3)
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

def move(board, pieces, info, N, K):
    # 1번 말부터 K번 말까지 순서대로 이동
    for i in range(K):
        if len(pieces[i])<1:
            continue

        # i+1 번째 말의 위치
        x, y, d = pieces[i]

        # 이동하려는 칸
        nx = x+dx[d]
        ny = y+dy[d]

        # 파란색 or 벗어나는 경우
        if (nx<0 or nx>=N or ny<0 or ny>=N) or board[nx][ny]==2:
            # 이동 방향 반대로
            d = (d-1)%4 if d%2==0 else (d+1)%4

            nx = x+dx[d]
            ny = y+dy[d]

            info[x][y][0][1] = d    # 방향 변경
            # 파란색 or 벗어나는 경우
            if (nx < 0 or nx >= N or ny < 0 or ny >= N) or board[nx][ny] == 2:
                # 이동 안하고 방향만 바꾸기
                pieces[i] = [x, y, d]
                continue

        # 빨간색
        if board[nx][ny]==1:
            # 그 말과 그 위에 있는 모든 말의 쌓여있는 순서 반대로
            info[x][y] = info[x][y][::-1]
            pieces[i] = []

            # 기존에 말이 있는 경우
            if info[nx][ny]:
                pieces[info[x][y][0][0]-1] = []
            else:
                pieces[info[x][y][0][0]-1] = [nx, ny, info[x][y][0][1]]

            info[nx][ny].extend(info[x][y])  # 기존에 있는 말 위에 쌓기
            info[x][y] = []

        # 흰색
        if board[nx][ny]==0:
            # 기존에 말이 있는 경우
            if info[nx][ny]:
                pieces[i] = []
            else:
                pieces[i] = [nx, ny, d]

            info[nx][ny].extend(info[x][y])   # 기존에 있는 말 위에 쌓기
            info[x][y] = []

        # 말이 4개 이상 쌓이는 경우 종료
        if len(info[nx][ny]) >= 4:
            return True

    return False


answer = -1
for turn in range(1, 1001):
    if move(board, pieces, info, N, K):
        answer = turn
        break
print(answer)

"""
N x N 인 체스판
K : 사용하는 말의 개수
각 칸 : 흰색(0), 빨간색(1), 파란색(2) 중 하나

이동방향 : 오른쪽(1), 왼쪽(2), 위(3), 아래(4)
턴 한번 : 1번 말부터 K번 말까지 순서대로 이동시킴
가장 아래에 있는 말만 이동 가능
말이 4개 이상 쌓이는 순간 게임 종료

흰색
    - 이동
빨간색
    - 이동, 순서 뒤집기
파란색 
    - 이동 방향 반대, 
    - 이동하려는 칸이 파란색 X : 한칸 이동
"""