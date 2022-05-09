'''
a[y-1][x-1]은 y-1번째 세로일 때 x-1번째 가로에서 x번째 가로로 이동할 수 있음

'''
import sys

def move():
    for i in range(n):
        num = i
        for j in range(h):
            if a[num][j]:
                num += 1
            elif a[num-1][j]:
                num -= 1
        if i != num:
            return 0
    return 1


def dfs(cnt, idx, r):
    global ans
    if cnt == r:
        if move():
            ans = cnt
        return

    for i in range(idx, h):
        for j in range(n-1):
            if a[j][i]: #다른 가로선과 겹치면 x
                continue
            if j - 1 >= 0 and a[j-1][i]: #가로선이 이어지면 안됨
                continue
            if j + 1 < n and a[j+1][i]:
                continue
            a[j][i] = 1
            dfs(cnt + 1, i, r)
            a[j][i] = 0

n, m, h = map(int, input().split())
a = [[0]*h for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    a[y-1][x-1] = 1

ans, flag = sys.maxsize, 1
for r in range(4):
    dfs(0, 0, r)
    if ans != sys.maxsize:
        print(ans)
        flag = 0
        break
if flag:
    print(-1)