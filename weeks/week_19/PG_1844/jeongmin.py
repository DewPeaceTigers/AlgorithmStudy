from collections import deque        

def solution(maps):
    
    n, m = len(maps), len(maps[0])
    
    # 남, 동, 북, 서
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    q = deque()
    q.append((0, 0))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            # 범위를 벗어나는 경우
            if nx<0 or n<=nx or ny<0 or m<=ny:
                continue
            
            # 벽이 있는 자리인 경우
            if maps[nx][ny] == 0:
                continue
            
            # 벽이 없는 자리인 경우
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y]+1
                q.append((nx, ny))
                
    answer = -1 if maps[n-1][m-1] == 1 else maps[n-1][m-1]  

    return answer