#하나씩 방문을 하면서 방문한 적 없는 경우(연결이 안되어있는 경우)
#count 증가

def solution(n, computers):
    answer = 0
    visited = [0] * n
    for i in range(n):
        if visited[i] == 0: #방문 안한 노드이면
            dfs(n, computers, i, visited) #연결 확인
            answer += 1

    return answer


def dfs(n, computers, index, visited):
    visited[index] = 1 #방문했다는 걸 표시
    for i in range(n):
        if index != i and computers[index][i] == 1: #index 노드와 연결 되어있는지 
            if visited[i] == 0: #방문 안한 경우
                dfs(n, computers, i, visited)