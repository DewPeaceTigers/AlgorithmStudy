## 민지

1. 최소 비용 신장 트리 조건

    사이클이 존재하면 안된다, 그래프 내의 모든 정점을 포함한다. 간선은 정점-1개 이다.
2. Kruskal 알고리즘 코드의 빈칸을 채워라
```python
v, e=map(int, input().split())

#부모 테이블 초기화
parent=[0]*(v+1)
for i in range(1, v+1):
    parent[i]=i

#find 연산
def find(node):
    if parent[node] ___ node:
        parent[node]=find(parent[node])
    return parent[node]

#union 연산
def union(node_v, node_e):
    root1=______________
    root2=______________
    if root1<root2:
        parent[root2]=root1
    else:
        parent[root1]=root2

total_cost=0
edges=[]

for _ in range(e):
    a, b, cost=map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for i in range(e):
    cost, a, b=edges[i]
    if find(parent, a) ____ find(parent, b):
        union(a, b)
        total_cost+=cost

print(total_cost)
```
1)!=
2) find(a)
3) find(b)
4) !=

3. 크루스칼 알고리즘에서 사이클의 발생 여부를 판단할때 사용하는 알고리즘은?

    union-find 알고리즘
4. 프림 알고리즘과 크루스칼 알고리즘의 차이점은?

    크루스칼 알고리즘은 가중치가 작은 간선에서 시작을 하고 프림 알고리즘은 특정 노드에서 시작을 해, 해당 노드에서 가중치가 가장 작은 간선을 통해 노드를 연결한다.

## 예리

1. 비용 트리의 조건은?

    사이클이 존재하면 안된다, 그래프 내의 모든 정점을 포함한다. 간선은 정점-1개 이다.

2. Kruskal Algorithm에서 두 노드를 연결할 때, 각 노드의 최상위 노드를 확인하는 이유는?

    사이클 발생 여부를 확인하기 위해서 이다
3. union 코드의 빈칸을 채워라

   ```python
   def find(node):
       # path compression 기법
       if parent[node] != node:
           parent[node] = find(parent[node])
       return parent[node]

   def union(node_v, node_u):
       root1 = '___'(node_v)
       root2 = '___'(node_u)

       # union-by-rank 기법
       if rank[root1] '___' rank[root2]:
           parent[root2] = root1
       else:
           parent[root1] = root2
           if rank[root1] == rank[root2]:
               rank[root2] += 1
   ```

   find, <

## 정민
 1. 신장트리란 무엇인가? 신장 트리의 간선의 개수는?

    
2. 유니온파인드의 find 연산입니다. 
    - 루트 노드에 더욱 빠르게 접근할 수 있는 기법으로 아래의 빈칸을 채워주세요.
    
    ```python
    # 특정 원소가 속한 집합을 찾기
    def find_parent(parent, x):
    	# 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
      if parent[x] !=x:
      	___________________________________
      return _____________
    ```
    
    parent[x]=find(parent, parent[x])
    parent[x]

3. O/X 문제입니다!
    
    1) 하나의 그래프에는 한 가지의 신장트리가 존재한다.
    X
    2) 크루스칼, 프림 알고리즘 모두 그리디 알고리즘으로 분류할 수 있다.
    O
4. 크루스칼과 프림 알고리즘의 차이점은?
    
    크루스칼 알고리즘은 가중치가 작은 간선에서 시작을 하고 프림 알고리즘은 특정 노드에서 시작을 해, 해당 노드에서 가중치가 가장 작은 간선을 통해 노드를 연결한다.
5. 크루스칼 알고리즘에서 사이클 생생 여부를 판단할 때 사용하는 알고리즘은?
    
    union-find 알고리즘