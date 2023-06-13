def solution(board, skill):
    answer = 0

    attacks = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]

    for s in skill:
        t, r1, c1, r2, c2, degree = s
        if t == 1:  # 공격
            degree *= -1

        attacks[r1][c1] += degree
        attacks[r1][c2 + 1] -= degree
        attacks[r2 + 1][c1] -= degree
        attacks[r2 + 1][c2 + 1] += degree

    # 열 누적합
    for i in range(len(attacks) - 1):
        for j in range(len(attacks[0]) - 1):
            attacks[i][j + 1] += attacks[i][j]

    # 행 누적합
    for i in range(len(attacks) - 1):
        for j in range(len(attacks[0]) - 1):
            attacks[i + 1][j] += attacks[i][j]

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += attacks[i][j]
            if board[i][j] > 0:
                answer += 1
    return answer