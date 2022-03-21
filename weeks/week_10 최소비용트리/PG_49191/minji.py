'''
못품
플로이드와샬을 이용
ex) a가 b를 이겼다면 b는 항상 a의 아래이고 b가 c를 이겼다면 c도 항상 b의 아래.
그럼 c는 항상 a의 아래이다.
'''
def solution(n, results):
    answer = 0
    board = [[0] * n for _ in range(n)]

    for a, b in results:
        board[a - 1][b - 1] = 1
        board[b - 1][a - 1] = -1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j or board[i][j] in [1, -1]:
                    continue
                if board[i][k] == board[k][j] == 1:
                    board[i][j] = 1
                    board[j][i] = board[k][i] = board[j][k] = -1
    for row in board:
        if row.count(0) == 1:
            answer += 1
    return answer