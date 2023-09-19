def solution(rows, cols, queries):
    answer = []
    boards = [[0]*cols for i in range(1,rows+1)]
    cnt = 0
    for i in range(rows):
        for j in range(cols):
            cnt+=1
            boards[i][j] = cnt
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    for [x1,y1,x2,y2] in queries:
        x1,y1,x2,y2 = x1-1,y1-1,x2-1,y2-1
        d = 0
        nx, ny = x1, y1
        before = boards[nx][ny]
        changed = []
        while d<4:
            changed.append(before)
            nx += dx[d]
            ny += dy[d]
            if not(x1<=nx<=x2 and y1<=ny<=y2):
                nx-=dx[d]
                ny-=dy[d]
                d+=1
                if d==4: break
                nx += dx[d]
                ny += dy[d]
            now = boards[nx][ny]
            boards[nx][ny]=before
            before = now
        answer.append(min(changed))
    return answer
