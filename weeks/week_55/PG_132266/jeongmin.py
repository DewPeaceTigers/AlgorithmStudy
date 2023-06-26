from collections import deque


def solution(n, roads, sources, destination):
    answer = [-1] * len(sources)

    # 길 정보 그래프로 저장
    graph = [[] for _ in range(n+1)]
    # 서로 왕복할 수 있으므로 양방향 그래프
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    # 부대원의 인덱스 정보
    sources_idx = {sources[i]: i for i in range(len(sources))}

    # sources에 destination이 포함되어 있다면 0으로 설정
    if destination in sources:
        answer[sources_idx[destination]] = 0

    # destination을 시작점으로 sources에 있는 부대원들까지의 최단거리 구하기
    q = deque()
    q.append((destination, 0))

    # 방문여부 관리
    visited = [False] * (n+1)
    visited[destination] = True

    while q:
        cur, dist = q.popleft()

        for x in graph[cur]:
            # 방문했던 부대원이면 넘어감
            if visited[x]:
                continue

            # sources 배열에 x가 포함될 때
            if x in sources:
                answer[sources_idx[x]] = dist+1

            visited[x] = True
            q.append((x, dist+1))

    return answer
