## 예리

1. DFS와 BFS의 차이점은?

   DFS는 자식부터 탐색하여 깊이 탐색하는 방식이다. 스택을 이용한다.
   BFS는 같은 레벨부터 탐색하여 넓게 탐색하는 방식이다. 큐를 이용한다.

2. DFS와 BFS의 시간 복잡도에 대해 설명하세요.

   모든 경우를 탐색하므로 노드와 간선의 개수 만큼 돌게 된다.
   O(노드 개수 + 간선 개수)

3. DFS 코드의 빈칸을 채우세요.

   ```python
   def dfs_iterative(start_v):
       discovered=[]
       stack=[start_v]
       while stack:
           v=stack.`   `
           if v not in discovered:
           discovered.append(v)
           for w in graph[v]:
               stack.append(w)
       return discovered
   ```

   pop()

4. 최단 거리를 구하는 문제에 적합한 것은 BFS이다. 답은 O/X로 표시하고, 이유를 설명하세요.

   O
   BFS는 같은 레벨부터 접근하게 되는데 가장 인접한 곳부터 간다. 가장 가까운 곳부터 가기 때문에 이를 통해 나오는 루트가 최단 거리일 수 밖에 없다.

5. DFS와 BFS는 대표적 '**\_\_**' 탐색 알고리즘이다.

   그래프
