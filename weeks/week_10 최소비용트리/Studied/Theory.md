# 최소 비용 신장 트리(Minimum Cost Spanning Tree)

가중치 무방향 그래프에서 모든 정점을 연결할 때 최소 비용으로 연결할 수 있는 방법을 찾는 알고리즘이다.

> 가중치 무방향 그래프
> 정점 사이에 가중치가 있고 간선에 방향이 없는 그래프

## 조건

1. 그래프 내의 모든 정점을 포함한다
2. 사이클이 존재해선 안 된다

## Kruskal(크루스칼) 알고리즘

간선을 기준으로 트리를 만드는 방법이다. 크루스칼 알고리즘은 간선들을 가중치가 증가하는 순서로 정렬하고 가중치가 가장 작은 간선이 사이클을 만들지 않으면 트리 간선으로 선택한다. 다음 가중치에서도 사이클을 만들지 않으면 트리 간선으로 선택하고 이 과정을 반복해서 정점-1개의 간선을 선택하는 알고리즘이다.

> 그리디 알고리즘
> 항상 욕심내서 최솟값을 선택하여 가중치의 합이 최소인 것을 찾기 때문에 그리디 알고리즘이라고 할 수 있다.

### 동작

1. 주어진 모든 간선 정보에 대해 간선 비용이 낮은 순서(오름차순)로 정렬을 수행한다
2. 정렬된 간선 정보를 하나씩 확인하면서 현재의 간선이 노드들 간의 사이클을 발생하는지 확인한다
3. 만약 사이클이 발생하지 않은 경우, 최소 신장 트리에 포함시키고 사이클이 발생한 경우 최소 신장 트리에 포함시키지 않는다
4. 1~3번 과정을 모든 간선 정보에 대해 반복 수행한다
   > 부모 테이블을 항상 가지고 있어야 한다.
   > 서로소 집합 알고리즘으로 루트를 찾기 위해서는 재귀적으로 부모를 거슬러 올라가야 한다.

## Union-Find 알고리즘(서로소 집합 알고리즘)

크루스칼 알고리즘에서 간선이 사이클을 만드는지를 파악하기 위해 사용한다. 이 알고리즘은 여러 노드가 존재할 때 두 개의 노드를 선택해 루트를 확인하고 현재 서로 같은 그래프에 속하는지 판별한다. 상호 배타적 집합들은 1차원 리스트로 표현하며 루트의 리스트 원소에는 루트 자신이 저장되고 루트가 아닌 노드의 원소에는 부모 노드가 저장된다.

> Disjoint Set<br/>
> 서로 중복되지 않는 부분 집합들로 나눠진 원소들에 대한 정보를 저장하고 조작하는 자료구조
> 즉, 공통 원소가 없는 "상호 배타적"인 부분 집합들로 나눠진 원소들에 대한 자료구조이다.

### Union

두 개의 집합을 하나의 집합으로 합치는 연산이다.

### Find

두 노드를 선택해 현재 노드가 서로 같은 그래프에 속하는지 판별하기 이해 각 그룹의 루트 노드를 확인한다. 루트 노드가 동일하면 사이클이 발생한다.

### 동작

초기화 : n개의 원소가 개별 집합으로 이뤄지도록 초기화
Union (연결)
두 개별 집합을 하나의 집합으로 합침
Find (사이클 유무)
여러 노드가 존재할 때, 두 노드를 선택해 현재 노드가 서로 같은 그래프에 속하는 지 판별하기 위해 각 그룹의 최상단 원소 즉 루트 노드를 확인
루트 노드가 동일 : 이미 연결, 부분 집합 ➡️ 사이클 발생

### 구현

시간복잡도: O(ElogE)

```python
v, e=map(int, input().split())

#부모 테이블 초기화
parent=[0]*(v+1)
for i in range(1, v+1):
    parent[i]=i

#find 연산
def find(node):
    if parent[node]!=node:
        parent[node]=find(parent[node])
    return parent[node]

#union 연산
def union(node_v, node_e):
    root1=find(node_v)
    root2=find(node_e)

    if root1<root2:
        parent[root2]=root1
    else:
        parent[root1]=root2

    # # union-by-rank 기법
    # if rank[root1] > rank[root2]:
    #     parent[root2] = root1
    # else:
    #     parent[root1] = root2
    #     if rank[root1] == rank[root2]:
    #         rank[root2] += 1

total_cost=0
edges=[]

for _ in range(e):
    a, b, cost=map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for i in range(e):
    cost, a, b=edges[i]
    if find(parent, a) != find(parent, b):
        union(a, b)
        total_cost+=cost

print(total_cost)
```

## Prim(프림) 알고리즘

시작 정점을 선택 후 최소 간선으로 연결된 노드를 연결하고 이 노드에서 다시 최소 간선으로 연결된 노드를 연결하는 방식으로 확장

> 크루스칼 알고리즘과의 차이<br/>
> 크루스칼 알고리즘: 가중치가 가장 작은 **간선**에서 시작<br/>
> 프림 알고리즘: 특정 **노드**에서 시작, 해당 노드에서 가중치가 가장 작은 간선을 통해 노드를 연결

### 과정

1. 임의의 노드를 선택 후 연결된 노드 집합에 삽입
2. 선택된 정점에 연결된 간선을 리스트로 만든다
3. 간선 리스트에서 가장 작은 가중치를 가진 간선부터 선택
   3-1. 이 간선에 연결된 노드가 연결된 노드 집합에 있으면 패스(Cycle 방지)
   3-2. 연결된 노드 집합에 없으면 해당 간선을 선택 후 최소 신장 트리에 삽입
4. 추출한 간선은 리스트에서 제거
5. 간선 리스트에 간선이 없어질 때까지 반복

### 구현

- collections 라이브러리의 defaultdict함수 활용
  시간 복잡도 : O(ElogE)

```python
from collections import defaultdict
from heapq import *

def prim(first_node, edges):
    mst = []
    # 해당 노드에 해당 간선을 추가
    adjacent_edges = defaultdict(list)
    for weight, node1, node2 in edges:
        adjacent_edges[node1].append((weight, node1, node2))
        adjacent_edges[node2].append((weight, node2, node1))

    # 처음 선택한 노드를 연결된 노드 집합에 삽입
    connected = set(first_node)
    # 선탠된 노드에 연결된 간선을 간선 리스트에 삽입
    candidated_edge = adjacent_edges[first_node]
    # 오름 차순으로 정렬
    heapify(candidated_edge)

    while candidated_edge:
        weight, node1, node2 = heappop(candidated_edge)
        # 사이클 있는지 확인 후 연결
        if node2 not in connected:
            connected.add(node2)
            mst.append((weight, node1, node2))

            for edge in adjacent_edges[node2]:
                if edge[2] not in connected:
                    heappush(candidated_edge, edge)

    return mst
```

- 개선된 알고리즘
  간선이 아닌 노드를 중심으로 우선순위 큐를 만들어서 풀어나간다 - 초기화
  선택한 [노드:key]구조를 만든 후 key 값을 0으로 입력한 후 나머지 노드의 key값은 무한대로 설정
  모든 [노드:key]값을 큐에 넣는다 - 가장 key값이 적은 [노드:key]를 pop으로 추출 - 해당 노드의 인접한 노드들에서 key 값과 가중치의 값을 비교하여 가중치 값이 작으면 해당 key값을 가중치 값으로 업데이트 - 업데이트 후 우선순위 큐에서 key값이 가장 작은 노드를 루트 노드로 올라오도록 해야함
  heapdict라이브러리 이용

```python
from heapdict import heapdict

def prim(graph, first):
    mst = []
    keys = heapdict()
    previous = dict()
    total_weight = 0

    #초기화
    for node in graph.keys():
        keys[node] = float('inf')
        previous[node] = None
    keys[first], previous[first] = 0, first

    while keys:
        current_node, current_key = keys.popitem()
        mst.append([previous[current_node], current_node, current_key])
        total_weight += current_key
        for adjacent, weight in graph[current_node].items():
            if adjacent in keys and weight < keys[adjacent]:
                keys[adjacent] = weight
                previous[adjacent] = current_node
    return mst, total_weight
```

## 크루스칼 vs 프림

둘다 그리디 알고리즘으로 분류됨
크루스칼 알고리즘은 가장 가중치가 작은 간선부터 선택하면서 MST 구함
프림 알고리즘은 특정 정점에서 시작, 해당 정점에 연결된 가장 가중치가 작은 간선을 선택, 간선으로 연결된 정점들에 연결된 간선 중에서 가장 가중치가 작은 간선을 선택하면서 MST 구함
