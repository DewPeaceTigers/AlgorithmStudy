"""
[틀린코드]
테스트케이스 7번 틀림!!

10 10 7
0 0 0 0 0 0 5 1 0 0
0 0 0 0 0 0 0 0 9 0
0 0 0 0 0 0 0 0 9 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 5 0 0

정답
50
3 5

내 출력
52
3 7
"""

from collections import deque
import heapq

N, M, K = map(int, input().split())

# 미로 정보
miro = [list(map(int, input().split())) for _ in range(N)]

# 참가자의 좌표
people = []
for _ in range(M):
    px, py = map(int, input().split())
    people.append((px-1, py-1))
    miro[px-1][py-1] -= 1

# 출구 좌표
ex, ey = map(int, input().split())
ex, ey = ex-1, ey-1
miro[ex][ey] = 10

# 회전할 정사각형 정보
rect_x, rect_y, rect_l = 0, 0, 0

# 모든 참가자들의 이동거리 합 저장
answer = 0


# 모든 참가자 이동
def people_move():
    global answer, miro, ex, ey

    new_pos = []
    for x, y in people:
        # 이동할 위치
        move_pos = []
        # 출구랑 거리가 가까운 위치 선정
        if x > ex:  # 위로 이동
            move_pos.append((x-1, y))
        if x < ex:  # 아래로 이동
            move_pos.append((x+1, y))
        if y > ey:  # 왼쪽으로 이동
            move_pos.append((x, y-1))
        if y < ey:  # 오른쪽으로 이동
            move_pos.append((x, y+1))

        # print("이동할 위치", nx, ny, miro[nx][ny])
        # 움직였는지 저장
        move = False
        for nx, ny in move_pos:
            # 벽이면 이동 불가능
            if 1 <= miro[nx][ny] <= 9:
                continue

            # 벽이 없는 곳으로 이동 가능
            move = True
            answer += 1

            # 출구가 아닌 경우 참가자 위치 갱신
            if (nx, ny) != (ex, ey):
                new_pos.append((nx, ny))
            break

        if not move:
            new_pos.append((x, y))

    # 참가자 이동 후 정보 갱신
    # 참가자 이동 전 위치 0 표시
    for x, y in people:
        miro[x][y] = 0
    # 참가자 이동 후 위치 -1 표시
    for x, y in new_pos:
        miro[x][y] -= 1

    return new_pos


# 8방향
dx = [-1, -1, 0, -1, 0, 1, 1, 1]
dy = [-1, 0, -1, 1, 1, -1, 0, 1]


def find_rect():  # 가장 작은 정사각형 찾기
    global ex, ey, rect_x, rect_y, rect_l

    visited = [[False]*N for _ in range(N)]

    q = []
    # (정사각형 길이, 출구 기준 상대위치, 행위치, 열위치)
    heapq.heappush(q, (1, 0, ex, ey))
    visited[ex][ey] = True

    while q:
        h, p, x, y = heapq.heappop(q)

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            # 경계 벗어나면 넘어감
            if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny]:
                continue

            # 참가자가 있는 경우
            if miro[nx][ny] < 0:
                # print("참가자 발견!!", nx, ny)
                # 가장 작은 정사각형 잡기
                c1, c2 = max(ex, nx)-h, max(ey, ny)-h
                rect_x = 0 if c1 < 0 else c1
                rect_y = 0 if c2 < 0 else c2
                rect_l = h+1
                return
                # if nx <= ex and ny <= ey: # 출구 기준 좌측 상단 정사각형
                #     return (ex-h if ex-h>=0 else 0, ey-h if ey-h>=0 else 0, h+1)
                # elif nx <= ex and ny > ey: # 출구 기준 우측 상단 정사각형
                #     return (ex-h if ex-h>=0 else 0, ey, h+1)
                # elif nx > ex and ny <= ey: # 출구 기준 좌측 하단 정사각형
                #     return (ex, ey-h if ey-h>=0 else 0, h+1)
                # else: # 출구 기준 우측 하단 정사각형
                #     return (ex, ey, h+1)

            if nx <= ex:
                prior = 1 if ny <= ey else 2
            else:
                prior = 3 if ny <= ey else 4

            heapq.heappush(q, (h+1, prior, nx, ny))
            visited[nx][ny] = True

# 미로 회전
# 정사각형 좌측 상단 좌표 : (r, c), 한변 길이 : h


def miro_rotate(r, c, h):
    global people, ex, ey

    # new_miro = [[miro[i][j] for j in range(N)] for i in range(N)]

    # 가장 바깥 테두리부터 회전
    x, y = r, c
    for k in range(h, 1, -2):
        tmp = miro[x][y:y+k]
        for i in range(k):  # 좌 -> 상
            miro[x][y+i] = miro[x+k-1-i][y]
        for i in range(k):  # 하 -> 좌
            miro[x+i][y] = miro[x+k-1][y+i]
        for i in range(k):  # 우 -> 하
            miro[x+k-1][y+i] = miro[x+k-1-i][y+k-1]
        for i in range(k):  # 상 -> 우
            miro[x+i][y+k-1] = tmp[i]

        x += 1
        y += 1

    new_pos = []
    # 회전 영역 정보 업데이트
    for i in range(N):
        for j in range(N):
            # 벽 내구도 -1
            if r <= i < r+h and c <= j < c+h and 0 < miro[i][j] < 10:
                miro[i][j] -= 1
            # 참가자 위치 갱신
            if miro[i][j] < 0:
                for x in range(-miro[i][j]):
                    new_pos.append((i, j))
            if miro[i][j] == 10:
                ex, ey = i, j

    people = new_pos


# K초 동안 과정 반복
for time in range(K):
    # print(time+1, "초 후")

    # 모든 참가자 이동
    people = people_move()
    # for i in range(N):
    #     print(*miro[i])
    # print("이동횟수:", answer)
    # print()
    # 모든 참가자가 탈출에 성공한다면 게임 끝!
    if len(people) == 0:
        break
    # 미로 회전
    find_rect()  # 가장 작은 정사각형 잡기
    miro_rotate(rect_x, rect_y, rect_l)  # 시계방향 90도 회전
    # for i in range(N):
    #     print(*miro[i])
    # print(people)
    # print("출구:", ex, ey)
    # print()

print(answer)
print(ex+1, ey+1)

"""
10 10 100
7 7 1 0 4 8 3 1 0 9
2 1 8 4 1 9 5 2 3 7
7 2 9 8 6 3 6 8 8 1
1 5 9 0 4 0 9 5 0 8
0 0 0 8 4 1 6 0 1 4
9 5 8 9 2 9 7 0 0 7
3 0 7 1 6 5 3 2 6 0
9 2 7 3 6 6 7 6 6 8
0 5 0 9 4 9 3 4 2 3
9 0 3 0 2 6 0 4 8 7
5 2
9 3
5 2
4 4
7 10
6 9
5 8
7 10
10 7
5 8
10 4

63
2 1
"""
