def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]

    def union(a, b):
        root1 = find(a)
        root2 = find(b)
        if root1 < root2:
            parent[root2] = root1
        else:
            parent[root1] = root2

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    for a, b, cost in costs:
        if find(a) != find(b):
            union(a, b)
            answer += cost
    return answer