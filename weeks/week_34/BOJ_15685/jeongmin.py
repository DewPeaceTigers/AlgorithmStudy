import sys

input = sys.stdin.readline

N = int(input())

points = set()

# 우, 상, 좌, 하
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

board = [[0]*100 for _ in range(100)]

# 드래곤 커브 생성
def curve():
    dg_points = [(x,y), (x+dx[d], y+dy[d])]

    for i in range(g):
        end = dg_points[-1]

        n = len(dg_points)-1
        for j in range(n-1, -1, -1):
            # print(j)
            # end와 차이
            tx = dg_points[j][0] - end[0]
            ty = dg_points[j][1] - end[1]

            # 90도 회전한 좌표
            nx = end[0] - ty
            ny = end[1] + tx

            dg_points.append((nx, ny))

        # print(dg_points)

    for p in dg_points:
        points.add(p)

for _ in range(N):
    x, y, d, g = map(int, input().split())
    curve()

# print(points)
answer = 0

rx = [-1, -1, 0, 0]
ry = [-1, 0, -1, 0]

for x, y in points:

    for i in range(4):
        nx = x + rx[i]
        ny = y + ry[i]

        if nx<0 or nx>=100 or ny<0 or ny>=100:
            continue

        board[ny][nx] += 1

        # 네 꼭지점을 모두 포함한 정사각형
        if board[ny][nx] == 4:
            answer += 1

# for i in range(10):
#     for j in range(10):
#         print(board[i][j], end=" ")
#     print()
print(answer)

"""
1
0 0 0 3
"""