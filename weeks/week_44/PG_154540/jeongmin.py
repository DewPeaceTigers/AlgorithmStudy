from collections import deque

def solution(maps):
    answer = []
    
    # 상, 하, 좌, 우     
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    R = len(maps)
    C = len(maps[0])
    
    # 방문 여부 저장 배열
    visited = [[False]*C for _ in range(R)]
        
    
    for i in range(R):
        for j in range(C):
            # 숫자라면 bfs 수행
            if maps[i][j] != 'X' and not visited[i][j]:
                visited[i][j] = True
                
                # 식량 합 저장
                food = int(maps[i][j])
                
                q = deque()
                q.append((i, j))
                while q:
                    r, c = q.popleft()

                    for k in range(4):
                        nr = r + dr[k]
                        nc = c + dc[k]

                        # 경계 체크
                        if nr<0 or nr>=R or nc<0 or nc>=C:
                            continue

                        # 방문한 적이 있거나 바다인 경우 넘어감
                        if visited[nr][nc] or maps[nr][nc]=='X':
                            continue

                        # 식량 추가
                        food += int(maps[nr][nc])
                        # 무인도에 땅 추가
                        q.append((nr, nc))
                        # 방문 처리
                        visited[nr][nc] = True

                answer.append(food)
    
    # 오름차순
    answer.sort()
    
    # 지낼 수 있는 무인도가 없다면
    if not answer:
        answer.append(-1)
    
    return answer