## dp.. 좌우 중 작은 것과 현재 중 작은 것을 고르기..
def solution(board):
    answer=0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]:
                board[i][j]+=min(min(board[i][j-1],board[i-1][j]),board[i-1][j-1])
            answer = max(answer,board[i][j])
    for b in board: print(b)

    return answer**2