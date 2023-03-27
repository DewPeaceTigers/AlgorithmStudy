from collections import defaultdict,deque
def solution(n, wires):
    answer = int(1e9)
    graph = defaultdict(list)
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    for i in range(len(wires)):
        a,b = wires[i] 
        graph[a].remove(b)
        graph[b].remove(a)
        q = deque([1])
        visit = [False]*(n+1)
        visit[1] = True
        area = 1
        while q:
            now = q.popleft()
            
            for next in graph[now]:
                if visit[next]: continue
                q.append(next)
                visit[next]=True
                area+=1
        answer = min(answer, abs(n-area-area))

        graph[a].append(b)
        graph[b].append(a)
    return answer