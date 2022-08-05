import sys

input = sys.stdin.readline

N = int(input())

home = [[0]*3 for i in range(N+1)]
home[0] = [0, 0, 0]

for i in range(1, N+1):
    # i-1번째 집을 빨강, 초록, 파랑으로 칠하는 비용
    preR, preG, preB = home[i - 1]
    
    # i번째 집을 빨강, 초록, 파랑으로 칠하는 비용
    r, g, b = map(int, input().split())

    home[i][0] = r + min(preG, preB)
    home[i][1] = g + min(preR, preB)
    home[i][2] = b + min(preR, preG)

print(min(home[N]))