from collections import deque
def solution(n, computers):
    answer = 0
    visited = [False]*len(computers)
    for i in range(len(computers)):
        if visited[i]: continue
        q= deque([i])
        visited[i]=True
        answer+=1
        while q:
            now = q.popleft()
            for j in range(len(computers[now])):
                if now==j: continue
                if computers[now][j]==1 and not visited[j]:
                    q.append(j)
                    visited[j]=True
        
    return answer