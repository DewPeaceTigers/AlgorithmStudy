import sys

input = sys.stdin.readline

# 게임이 끝난 상태인지 확인


def finish(board):
    # 가로 3칸
    for i in range(3):
        if board[3*i] != '.' and board[3*i] == board[3*i+1] == board[3*i+2]:
            return True

    # 세로 3칸
    for i in range(3):
        if board[i] != '.' and board[i] == board[3+i] == board[6+i]:
            return True

    # 대각선 3칸
    if board[0] != '.' and board[0] == board[4] == board[8]:
        return True
    if board[2] != '.' and board[2] == board[4] == board[6]:
        return True

    return False


while True:
    board = input().rstrip()

    # 입력의 마지막일 경우
    if board == "end":
        break

    # X, O 개수 차이는 최대 1
    cntX, cntO = board.count('X'), board.count('O')
    if cntX-cntO < 0 or cntX-cntO > 1:
        print('invalid')
        continue

    # 빈칸이 있는 경우에는 게임이 무조건 종료되어야 valid한 경우임
    final = finish(board)
    if board.count('.') > 0 and not final:
        print('invalid')
        continue

    valid = False

    # 제외할 말
    x = 'O' if cntX-cntO == 0 else 'X'
    # 'O' or 'X' 중에 하나 빼고 확인
    for i in range(9):
        if board[i] == x:
            tmp = [board[j] if j != i else '.' for j in range(9)]
            if not finish(tmp):
                # print(tmp)
                valid = True

    print('valid' if valid else 'invalid')
