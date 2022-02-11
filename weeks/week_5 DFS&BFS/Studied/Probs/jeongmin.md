## 정민

1. DFS, BFS를 구현할 때 사용하는 자료구조
    
    DFS: 스택, BFS: 큐
    
2. 다음 그래프를 DFS, BFS로 탐색했을 때 노드 방문 순서

    <img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/6839039c-c760-4f97-a53e-c8c53462396d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220210T091320Z&X-Amz-Expires=86400&X-Amz-Signature=94f59b36f999a992fa33c82539d785634c4cd46ed3030c9f0a0b3d13d578c5cb&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject"/>

    DFS: 1 → 2 → 4 → 5 → 8 → 3 → 6 → 7

    BFS: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8

3. 그래프를 구현하는 방법 2가지와 메모리, 속도 측면에서의 차이점

    - 인접 리스트
        - 모든 관계를 저장하므로 노드 개수가 많을 수록 메모리가 불필요하게 낭비됨
        - 특정한 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도 빠름
    - 인접 행렬
        - 연결된 정보만 저장하므로 메모리를 효율적으로 사용
        - 특정한 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도 느림

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
