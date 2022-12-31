import sys
import heapq

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = 0
while True:
    N = int(input())

    if N == 0:
        break

    cave = [list(map(int, input().split())) for _ in range(N)]
    d = [[1e9]*N for _ in range(N)]

    q = []
    heapq.heappush(q, [cave[0][0], 0, 0])
    d[0][0] = cave[0][0]

    while q:
        now, x, y = heapq.heappop(q)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue

            if now + cave[nx][ny] < d[nx][ny]:
                d[nx][ny] = now + cave[nx][ny]
                heapq.heappush(q, [d[nx][ny], nx, ny])

    T += 1
    print("Problem {}: {}".format(T, d[N-1][N-1]))