## 예리

1. 비용 트리의 조건은?

- 모든 노드가 연결돼있어야 함
- 사이클이 없어야 한다는 트리의 조건을 만족해야 함

2. Kruskal Algorithm에서 두 노드를 연결할 때, 각 노드의 최상위 노드를 확인하는 이유는?

   최상위 노드가 서로 같다면 사이클이 발생하기 때문에 확인해야한다.

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

   find, find, >
