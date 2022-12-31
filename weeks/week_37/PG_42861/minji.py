def find(parent, a):
    if parent[a] == a:
        return a
    return find(parent, parent[a])


def union(parent, a, b):
    root1 = find(parent, a)
    root2 = find(parent, b)
    if root1 < root2:
        parent[root2] = root1
    else:
        parent[root1] = root2


def solution(n, costs):
    answer = 0
    parent = [x for x in range(n)]

    costs.sort(key=lambda x: x[2])
    for cost in costs:
        if find(parent, cost[0]) != find(parent, cost[1]):
            union(parent, cost[0], cost[1])
            answer += cost[2]

    return answer