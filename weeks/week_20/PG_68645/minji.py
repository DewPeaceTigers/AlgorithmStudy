def solution(n):
    answer = []
    res = [[0] * n for _ in range(n)]
    num = 1
    x, y = -1, 0

    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            res[x][y] = num
            num += 1
    for i in range(n):
        for j in range(n):
            if res[i][j] > 0:
                answer.append(res[i][j])
    return answer