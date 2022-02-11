'''[풀이]
bfs 이용
- visited 리스트로 방문 여부 저장
- visited[i]가 0인 경우 네트워크 수 +1
- i와 연결된 컴퓨터 모두 방문 처리
'''

from collections import deque

ans = 0
def bfs(n, graph, computers):
    global ans
    
    visited = [0] * n
    
    for i in range(n):
        q = deque()
        
        if visited[i]==0:
            visited[i]=1
            ans+=1
            q.append(graph[i])
            while q:
                v = q.popleft()
                for j in range(len(v)):        
                    if visited[v[j]]==0:
                        visited[v[j]]=1
                        q.append(graph[v[j]])
    
def solution(n, computers):
    graph = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if computers[i][j]==1 and i!=j:
                graph[i].append(j)
                
    print(graph)
    bfs(n, graph, computers)
    
    answer = ans
    return answer