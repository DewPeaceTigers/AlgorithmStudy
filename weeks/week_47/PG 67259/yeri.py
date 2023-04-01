from collections import deque
        
def solution(board):
    answer = int(1e9)
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    length = len(board)
    q = deque([[0,0,-1]])
    dp = [[[int(1e9)]*4 for _ in range(length)] for _ in range(length)]
    dp[0][0]=[-1,-1,-1,-1]
    while q:
        x,y,bef = q.popleft()
        if x ==length-1 and y==length-1:
            answer = min(answer,dp[x][y][bef])
            continue

        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]

            if not (-1<nx<length and -1<ny<length) or board[nx][ny]==1: continue
            if bef!=-1:
                add = dp[x][y][bef] + (100 if d%2==bef%2 else 600)
            else:
                add = 100
            if dp[nx][ny][d] > add:
                dp[nx][ny][d] = add
                q.append([nx,ny, d])
    return answer