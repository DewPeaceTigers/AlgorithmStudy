from collections import deque

def solution(n, computers):
    answer = 0
    
    graph = [[] for _ in range(n)]
    for i in range(n):
        graph[i] = [x for x in range(n) if x!=i and computers[i][x]==1]
    
    # 방문여부 저장
    visited = [False] * n
    for i in range(n):
        # 방문했던 곳이라면 넘어감
        if visited[i]:
            continue
        
        # 방문했던 곳이 아닌 경우 네트워크 하나 추가
        answer += 1
        
        # bfs 수행
        q = deque()
        q.append(i)
        
        while q:
            cur = q.popleft()
            
            for x in graph[cur]:
                if visited[x]:
                    continue
                
                # 네트워크 연결된 곳 방문 처리
                visited[x] = True
                q.append(x)
            
    return answer