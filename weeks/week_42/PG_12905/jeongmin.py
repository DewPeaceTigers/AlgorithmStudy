def solution(board):
    answer = 1 if board[0][0] else 0 
    
    N = len(board)
    M = len(board[0])
    
    for i in range(1, N):
        for j in range(1, M):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
                
                answer = max(answer, board[i][j])
    
    return answer**2