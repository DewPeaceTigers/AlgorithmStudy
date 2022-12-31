""" 크루스칼 알고리즘 사용!! """

# 특정 원소가 속한 집합 찾기
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    answer = 0
    
    parent = [i for i in range(n)]
    
    # 비용순으로 정렬
    costs.sort(key = lambda x: x[2])
    
    # 간선 하나씩 확인
    for edge in costs:
        a, b, cost = edge
        
        # 사이클이 발생하지 않는 경우에만 포함
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            answer += cost
    
    return answer