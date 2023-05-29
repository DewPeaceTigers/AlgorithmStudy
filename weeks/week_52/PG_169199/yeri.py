from collections import deque
def solution(board):
    answer = 0
    start = []
    end = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'R':
                start = [i,j]
            if board[i][j] == 'G':
                end = [i,j]
    q = deque([[start,0]])
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    count = [[int(1e9)]*len(board[0]) for _ in range(len(board))]
    count[start[0]][start[1]] = 0
    while q:
        [x,y], cnt = q.popleft()
        if [x,y] == end: 
            answer = count[end[0]][end[1]]
            break
        
        for d in range(4):
            cx,cy = x,y
            while True:
                cx += dx[d]
                cy += dy[d]
                if not(-1<cx < len(board) and -1<cy<len(board[0])) or board[cx][cy] == 'D':
                    cx -= dx[d]
                    cy -= dy[d]
                    break
            if cnt + 1 < count[cx][cy]:
                count[cx][cy] = cnt +1
                q.append([[cx,cy], cnt+1])
    return answer if answer !=0 else -1
