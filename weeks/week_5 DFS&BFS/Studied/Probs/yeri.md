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

---

## 민지

1. BFS와 DFS란

   예리1

2. BFS와 DFS에서 사용하는 자료구조(각각)

   BFS는 큐를, DFS는 스택을 사용한다.

3. BFS와 DFS 중 최단 거리를 구할 때 사용하는 자료 구조

   예리4

4. BFS와 DFS 중 재귀적으로 동작하는 알고리즘은?

   DFS

5. BFS와 DFS의 시간 복잡도

   예리2

---

## 정민

1. DFS, BFS를 구현할 때 사용하는 자료구조

   민지 2

2. 다음 그래프를 DFS, BFS로 탐색했을 때 노드 방문 순서
   <img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/6839039c-c760-4f97-a53e-c8c53462396d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220210T091320Z&X-Amz-Expires=86400&X-Amz-Signature=94f59b36f999a992fa33c82539d785634c4cd46ed3030c9f0a0b3d13d578c5cb&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject"/>

   - DFS: 1, 2, 4, 5, 6, 3, 6, 7
   - BFS: 1, 2, 3, 4, 5, 6, 7, 8

3. 그래프를 구현하는 방법 2가지와 메모리, 속도 측면에서의 차이점

   - 인접 행렬
     - 메모리 : 2차원 배열을 모두 저장하므로 낭비
     - 속도 : O(1), 연결 정보 조회시 빠르다. 모든 정점들의 간선 정보를 저장해두었기 때문이다.
   - 인접 리스트
     - 메모리 : 필요한 만큼의 공간만 사용
     - 속도 : O(n), 연결 정보 조회시 모두 탐색해야함.

4. DFS와 BFS의 시간 복잡도
   예리 2

5. 다음 문제를 풀기 위해 DFS, BFS 중 적합한 방법

   1)그래프의 **모든 정점을 방문**하는 것이 주요한 문제

   - DFS, BFS

     2)**경로의 특징**을 저장해둬야 하는 문제

   - DFS

     3)**최단거리** 구해야 하는 문제

   - BFS
