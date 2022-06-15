## 민지
1. BFS와 DFS란

    DFS는 루트노드에서 시작해서 다음 branch로 넘어가기 전에 해당 branch를 완벽하게 탐색하는 방법이고 BFS란 루트 노드에서 시작해서 인접한 노드를 먼저 탐색하는 방법이다. 

2. BFS와 DFS에서 사용하는 자료구조(각각)

    BFS에서는 주로 큐를 사용하고 DFS에서는 주로 스택을 사용한다

3. BFS와 DFS 중 최단 거리를 구할 때 사용하는 자료 구조

    BFS

4. BFS와 DFS 중 재귀적으로 동작하는 알고리즘은?

    DFS

5. BFS와 DFS의 시간 복잡도

    인접행렬을 사용하는 경우는 O(정접의 개수 ^2)
    
    인접리스트를 사용하는 경우는 O(정점의 개수+간선의 개수)

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

## 정민

1. DFS, BFS를 구현할 때 사용하는 자료구조
    
    DFS: 스택, BFS: 큐
    
2. 다음 그래프를 DFS, BFS로 탐색했을 때 노드 방문 순서

    <img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/6839039c-c760-4f97-a53e-c8c53462396d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220210T091320Z&X-Amz-Expires=86400&X-Amz-Signature=94f59b36f999a992fa33c82539d785634c4cd46ed3030c9f0a0b3d13d578c5cb&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject"/>

    DFS: 1 → 2 → 4 → 5 → 8 → 3 → 6 → 7

    BFS: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8

3. 그래프를 구현하는 방법 2가지와 메모리, 속도 측면에서의 차이점

    - 인접 리스트
        - 연결된 정보만 저장하므로 메모리를 효율적으로 사용
        - 특정한 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도 느림
    - 인접 행렬
        - 모든 관계를 저장하므로 노드 개수가 많을 수록 메모리가 불필요하게 낭비됨
        - 특정한 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도 빠름
        

4. DFS와 BFS의 시간 복잡도 

    (정점의 개수: V , 간선의 개수: E)

    - 인접 리스트의 경우 : O(V+E)
    - 인접 행렬의 경우 :  O(V^2)

5. 다음 문제를 풀기 위해 DFS, BFS 중 적합한 방법
    
    1)그래프의 **모든 정점을 방문**하는 것이 주요한 문제 → DFS, BFS 상관 X, 둘다 괜찮다.

    2)**경로의 특징**을 저장해둬야 하는 문제 → DFS

        각 정점에 숫자가 적혀있고 a부터 b까지 가는 경로를 구하는데 경로에 같은 숫자가 있으면 안 된다는 문제 등, 각각의 경로마다 특징을 저장해둬야 할 때는 DFS를 사용

    3)**최단거리** 구해야 하는 문제 → BFS 

        BFS는 현재 노드에서 가까운 곳부터 찾기 때문에 경로를 탐색 시 먼저 찾아지는 해답이 곧 최단거리이다.