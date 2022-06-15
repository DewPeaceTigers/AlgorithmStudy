from collections import deque, defaultdict

def bfs(start, nomore, n, route_):
    q = deque([start])
    visit = [False] * (n + 1)
    visit[start] = True
    visit[nomore] = True  # 연결 제외
    length = 1
    while q:
        front = q.popleft()
        for next in route_[front]:
            if not visit[next]:
                q.append(next)
                visit[next]=True
                length += 1
    return length

def solution(n, wires):
    answer = -1
    route_ = defaultdict(list)
    for a, b in wires:
        route_[a].append(b)
        route_[b].append(a)
    small_gap = 101
    for i, [a, b] in enumerate(wires):
        small_gap = min(small_gap, abs(bfs(a, b, n, route_) - bfs(b, a, n, route_)))
    return small_gap