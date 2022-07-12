def solution(board):
    n = len(board)
    m = len(board[0])

    # dp �غ�
    dp = [[0]*m for _ in range(n)]
    dp[0] = board[0]
    for i in range(1,n):
        dp[i][0] = board[i][0]
    
    # 2�� �������� ����
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    
    # �ִ� ���� ���ϱ�
    answer = 0
    for i in range(n):
        temp = max(dp[i])
        answer = max(answer, temp)
    
    return answer**2