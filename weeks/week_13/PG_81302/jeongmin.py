from collections import deque

def check(p, place):
    # 방문 여부
    visited = [[False]*5 for _ in range(5)]
    
    # 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque()
    q.append(p)
    cnt = 0
    while q:
        x, y = q.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어나는 경우
            if nx<0 or nx>4 or ny<0 or ny>4 or visited[nx][ny]:
                continue     

            # 값이 P값인 경우
            if place[nx][ny] == 'P':
                return 0

            if place[nx][ny] == 'O' and cnt == 0:
                q.append((nx, ny))
        cnt +=1
    return 1
                

def solution(places):
    answer = []
    
    for place in places:
        people = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    people.append((i, j))

        distance = 1
        for p in people:
            if not check(p, place):
                distance = 0
                break
        answer.append(distance)
        
    return answer