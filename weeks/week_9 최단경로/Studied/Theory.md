# 트리
정점과 간선을 이용해 사이클이 이루어지지 않게 구성된 자료 구조

## 특징
- 계층 모델
- 비순환 그래프
- 트리 내에 하위 트리가 있는 재귀적 자료구조
- 노드 N이면 트리는 N-1개 간선을 가짐
- Pre-oreder, In-order, Post-order
- 이진 트리, 이진 탐색 트리, 균형 트리, 이진 힙

## 용어
- Node : 데이터를 저장하는 기본 요소 (연결된 노드에 대한 간선 정보도 포함)
- Root Node : 트리 맨 위에 있는 노드
- Level : 노드의 깊이
- Parent node, Child node
- Leaf node (Terminal node) : child가 하나도 없는 노드
- Sibling : 동일한 Parent
- Depth : 트리에서 node가 가질 수 있는 최대 level

## 응용
### 이진 트리
노드의 최대 branch가 2인 트리

### 이진 탐색 트리 BST
- 이진 트리 + 추가적인 조건
- 조건 : 왼쪽 노드는 해당 노드보다 작은 값, 오른쪽 노드는 해당 노드보다 큰 값을 가지고 있음
- 용도 : 데이터 검색
- 특징
  - 장점: 탐색 속도 개선할 수 있음
  - 단점
    - 노드 삭제가 어려움. 
    - 평균 시간 복잡도는 O(logn)이지만, 트리가 균형잡히지 않으면 O(n)으로 연결 리스트와 동일한 성능을 보인다.
    
    
# 그래프
정점과 간선으로 이루어진 자료구조이다. 
### 구현 방법
- 인접 행렬
  그래프의 노드를 2차원 배열로 만든 것이다. 인접한 정점이라면 1, 아니면 0을 저장한다.
  - 장점 
    - 2차원 배열 안에 모든 정점들의 간선 정보를 담기 때문에 배열의 위치를 확인하면 두 점에 대한 연결 정보를 조회할 때 O(1) 의 시간 복잡도면 가능하다
    - 구현이 비교적 간단하다
  - 단점
    - 모든 정점에 대해 간선의 정보를 입력해야 하므로 O(n^2)의 시간복잡도가 소요된다
    - 무조건 2차원 배열이 필요하므로 필요 이상의 공간이 낭비된다
- 인접 리스트
  그래프의 노드들을 리스트로 표현한것입니다. 주로 정점의 리스트 배열을 만들어 관계를 설정해줌으로써 구현합니다. 
  - 장점
    - 정점들의 연결 정보를 탐색할 때 O(n)의 시간이면 가능하다
    - 필요한 공간만큼만 사용하기 때문에 공간 낭비가 적다 
  - 단점
    - 특정 두 점이 연결되어있는지를 확인하려면 인접행렬에 비해 시간이 오래 걸린다
    - 구현이 비교적 어렵다

## 그래프와 차이
![](https://images.velog.io/images/kinnyeri/post/c40b97be-52ce-4b4c-ad11-34e97277f79e/image.png)


### 최단 경로 문제란?
가중 그래프에서 간선의 가중치의 합이 최소가 되는 문제

### 최단 경로 문제의 종류
- 단일 출발 (single-source) 최단 경로
  - 어떤 하나의 정점에서 출발하여 나머지 모든 정점까지의 최단 경로를 찾는 문제
- 단일 도착 (single-destination) 최단 경로
  - 모든 정점에서 출발하여 어떤 하나의 정점까지의 최단 경로를 찾는 문제
  - 그래프 내의 간선들을 뒤집으면 단일 출발 최단 거리 문제로 바뀔 수 있음
- 단일 쌍 (single-pair) 최단 경로
  - 모든 정점 쌍들 사이의 최단 경로를 찾는 문제
  
### 주요 알고리즘
- BFS (완전탐색 알고리즘)
  - 가중치가 없거나 모든 가중치가 동일한 그래프에서 최단 경로를 구하는 경우 가장 빠름

- 다익스트라 알고리즘 (Dijkstra Algorithm)
  - 음이 아닌 가중 그래프에서의 단일 쌍, 단일 출발, 단일 도착 최단 경로 문제

- 플로이드-워셜 알고리즘 (Floyd-Warshall Algorithm)
  - 전체 쌍 최단 경로 문제

- 벨만-포드 알고리즘 (Bellman-Ford-Moore Algorithm)
  - 가중 그래프에서의 단일 쌍, 단일 출발, 단일 도착 최단경로

## 다익스트라 알고리즘 (Dijkstra Algorithm)
V개의 정점과 **음수가 아닌** E개의 간선을 가진 그래프 G에서 특정 출발 정점(S)에서부터 다른 모든 정점까지의 최단 경로를 구하는 알고리즘
- **그리디 알고리즘**으로 분류됨
: 매 상황에서 **가장 비용이 적은 노드를 선택**해 임의의 과정을 반복한다
- 단계를 거치며 한 번 처리된 노드의 최단 거리는 고정되어 더 이상 바뀌지 않는다
: 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해할 수 있다

### 동작 과정
1. 출발 노드를 설정한다
2. 최단 거리 테이블을 초기화한다.
3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
5. 위 과정에서 3번과 4번을 반복한다.

### 구현 방법
- **반복문** 사용
  🕰 시간 복잡도 : ``O(V^2)``
  - 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 매 단계마다 1차원 테이블의 모든 원소를 확인(순차 탐색)함
  
  - python 코드
  ```python
  import sys
  input = sys.stdin.readline
  INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

  # 노드의 개수, 간선의 개수를 입력받기
  n, m = map(int, input().split())
  # 시작 노드 번호를 입력받기
  start = int(input())
  # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
  graph = [[] for i in range(n + 1)]
  # 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
  visited = [False] * (n + 1)
  # 최단 거리 테이블을 모두 무한으로 초기화
  distance = [INF] * (n + 1)

  # 모든 간선 정보를 입력받기
  for _ in range(m):
      a, b, c = map(int, input().split())
      # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
      graph[a].append((b, c))

  # 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
  def get_smallest_node():
      min_value = INF
      index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
      for i in range(1, n + 1): # 선형 탐색
          if distance[i] < min_value and not visited[i]:
              min_value = distance[i]
              index = i
      return index

  def dijkstra(start):
      # 시작 노드에 대해서 초기화
      distance[start] = 0
      visited[start] = True
      for j in graph[start]:
          distance[j[0]] = j[1]
      # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
      for i in range(n - 1):
          # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
          now = get_smallest_node()
          visited[now] = True
          # 현재 노드와 연결된 다른 노드를 확인
          for j in graph[now]:
              cost = distance[now] + j[1]
              # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
              if cost < distance[j[0]]:
                  distance[j[0]] = cost

  # 다익스트라 알고리즘을 수행
  dijkstra(start)

  # 모든 노드로 가기 위한 최단 거리를 출력
  for i in range(1, n + 1):
      # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
      if distance[i] == INF:
          print("INFINITY")
      # 도달할 수 있는 경우 거리를 출력
      else:
          print(distance[i])
  ```

- **우선순위 큐** 사용(힙 자료구조 사용) ➱ 개선된 다익스트라 알고리즘
  🕰 시간 복잡도 : ``O(ElogV)`` (E : 간선의 개수, V : 노드의 개수)
  - 우선순위 큐는 현재 가장 가까운 노드를 저장하기 위한 목적으로 사용
  
  - python 코드
  ``` python
  import heapq
  import sys
  input = sys.stdin.readline
  INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

  # 노드의 개수, 간선의 개수를 입력받기
  n, m = map(int, input().split())
  # 시작 노드 번호를 입력받기
  start = int(input())
  # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
  graph = [[] for i in range(n + 1)]
  # 최단 거리 테이블을 모두 무한으로 초기화
  distance = [INF] * (n + 1)

  # 모든 간선 정보를 입력받기
  for _ in range(m):
      a, b, c = map(int, input().split())
      # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
      graph[a].append((b, c))

  def dijkstra(start):
      q = []
      # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
      heapq.heappush(q, (0, start))
      distance[start] = 0
      while q: # 큐가 비어있지 않다면
          # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
          dist, now = heapq.heappop(q)
          # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
          if distance[now] < dist:
              continue
          # 현재 노드와 연결된 다른 인접한 노드들을 확인
          for i in graph[now]:
              cost = dist + i[1]
              # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
              if cost < distance[i[0]]:
                  distance[i[0]] = cost
                  heapq.heappush(q, (cost, i[0]))

  # 다익스트라 알고리즘을 수행
  dijkstra(start)

  # 모든 노드로 가기 위한 최단 거리를 출력
  for i in range(1, n + 1):
      # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
      if distance[i] == INF:
          print("INFINITY")
      # 도달할 수 있는 경우 거리를 출력
      else:
          print(distance[i])
  ```

## 플로이드-워셜 알고리즘 (Floyd-Warshall Algorithm)
V개의 정점과 E개의 간선을 가진 가중 그래프 G에서 모든 정점 사이의 최단 경로를 구하는 알고리즘
- **다이나믹 프로그래밍**으로 분류됨
- 다익스트라 알고리즘과 마찬가지로 단계별로 거쳐가는 노드들을 기준으로 알고리즘을 수행함
  - 다만 매 단계마다 방문하지 않은 노드 중에 최단 거리를 갖는 노드를 찾는 과정이 필요 ❌ 
- '**거쳐가는 정점**' 을 기준을 최단 거리를 구하는 것
	: 각 단계마다 특정한 노드 𝑘를 거쳐가는 경우를 확인함
  - 𝑎에서 𝑏로 가는 최단 거리보다 𝑎에서 𝑘를 거쳐 𝑏로 가는 거리가 더 짧은지 검사
- 2차원 테이블에 최단 거리 정보를 저장
- 음의 간선도 사용 가능

> 점화식 : `D[a][b] = min(D[a][b],D[a][k]+D[k][b])`

### 구현
- 자료구조 생성, 초기화 
  1. INF 값 설정  
`INF = 노드개수 * 최대가중치 +1 `  
    > INF 값은?  
    INF = 노드개수 * 최대가중치 +1   
    ⬇️  
    1~N모드에서 모든 노드로 최대가중치로 이동하는 경우 - 자기자신으로 이동하는 경우 보다 큰 값으로 잡아야 버틸 수 있음. 위의 식은 안전한 값을 공식화 한 것  

    **DONT DO THIS**  
    1.INF = sys.maxsize : 연산에 시간이 오래걸려서 시간초과 발생 가능  
    2. int(1e9) : 극단적인 케이스에서 버틸 수 없음  

  2. 최단거리 테이블 전체를 INF 로 초기화  
`arr = [[INF j in range(n)] for i in range(n)]`
  3. 자기 자신으로 향하는 비용은 0으로 초기화  
  4. a→b, b→a 로의 비용 입력  

- 메인 로직	
  - 3중 포문 수행하며 DP테이블(arr) 갱신
    ```python
    for k in range(n):
        for i in range(n):
        for j in range(n):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
    ```

### 구현 방법
- 삼중 반복문 이용
  🕰 시간복잡도 : ``O(N^3)``
  - 노드의 개수가 N개일 때 알고리즘 상으로 N번의 단계를 수행
  - 각 단계마다 O(N^2)의 연산을 통해 현재 노드를 거쳐가는 모든 경로를 고려함
  
  - python 코드
  ``` python
  INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

  # 노드의 개수 및 간선의 개수를 입력받기
  n = int(input())
  m = int(input())
  # 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
  graph = [[INF] * (n + 1) for _ in range(n + 1)]

  # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
  for a in range(1, n + 1):
      for b in range(1, n + 1):
          if a == b:
              graph[a][b] = 0

  # 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
  for _ in range(m):
      # A에서 B로 가는 비용은 C라고 설정
      a, b, c = map(int, input().split())
      graph[a][b] = c

  # 점화식에 따라 플로이드 워셜 알고리즘을 수행
  for k in range(1, n + 1):
      for a in range(1, n + 1):
          for b in range(1, n + 1):
              graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

  # 수행된 결과를 출력
  for a in range(1, n + 1):
      for b in range(1, n + 1):
          # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
          if graph[a][b] == 1e9:
              print("INFINITY", end=" ")
          # 도달할 수 있는 경우 거리를 출력
          else:
              print(graph[a][b], end=" ")
      print()
  
  ```


## 벨만-포드 알고리즘 (Bellman-Ford-Moore Algorithm)
V개의 정점과 E개의 간선을 가진 가중 그래프 G에서 특정 출발 정점(S)에서 부터 다른 모든 정점까지의 최단 경로를 구하는 알고리즘

- 매 단계마다 모든 간선을 전부 확인하면서 모든 노드 간의 최단 거리를 구함 

### 동작 과정
1. 출발 노드를 설정한다.
2. 최단 거리 테이블을 초기화한다.
3. 다음의 과정을 (V(=정점)-1)번 반복한다.
    1. 모든 간선 E개를 하나씩 확인한다.
    2. 각 간선을 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
    
> 만약 음수 간선 순환이 발생하는지 체크하고 싶다면 3번 과정을 한 번 더 수행한다.
→ 이때 최단 거리 테이블이 갱신된다면 음수 간선 순환이 존재하는 것이다.
- V번째 단계에서 최단 거리 테이블이 갱신 여부로 음수 간선 순환을 확인 가능
(V - 1까지 단계를 진행하면 모든 노드에 대한 최단 거리가 확정된다.)

### 구현 방법
- 반복문 사용
  🕰 시간 복잡도 : ``O(VE)`` (E : 간선의 개수, V : 노드의 개수)

  - python 코드
  ``` python
  import sys
  input = sys.stdin.readline
  INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

  def bf(start):
      # 시작 노드에 대해서 초기화
      dist[start] = 0

      # 전체 n번의 라운드(round)를 반복
      for i in range(n):
          # 매 반복마다 '모든 간선'을 확인하며
          for cur in range(n):
              for (next_node, cost) in graph[cur]:
                  # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧을 경우
                  if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                      dist[next_node] = dist[cur] + cost

                      # n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                      if i == n-1:
                          return True

      return False

  # 노드의 개수, 간선의 개수를 입력받기
  n, m = map(int, input().split())

  # 모든 간선에 대한 정보를 담는 리스트 만들기
  graph = [[] for _ in range(n+1)]

  # 최단 거리 테이블을 모두 무한으로 초기화
  dist = [INF] * (n+1)

  # 모든 간선 정보를 입력받기
  for _ in range(m):
      a, b, c = map(int, input().split())
      # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
      graph[a].append((b, c))

  # 벨만 포드 알고리즘을 수행
  negative_cycle = bf(1) # 1번 노드가 시작 노드

  if negative_cycle:
      print('-1')
  else:
      # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리 출력
      for i in range(2, n+1):
          # 도달할 수 없는 경우, -1을 출력
          if dist[i] == INF:
              print('-1')
          # 도달할 수 있는 경우 거리를 출력
          else:
              print(dist[i])
  ```
  ```python
  import sys
  input = sys.stdin.readline
  INF = int(1e9)

  n, m = map(int, input().split())
  edges = []
  dist = [INF] * (1+n)

  for i in range(m):
      a, b, c = map(int, input().split())
      edges.append((a, b, c))

  def bf(start):
      dist[start] = 0
      for i in range(n):
          for j in range(m):
              cur = edges[j][0]
              next_node = edges[j][1]
              cost = edges[j][2]
              if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                  dist[next_node] = dist[cur] + cost
                  if i == n-1:
                      return True
      return False

  negative_circle = bf(1)

  if negative_circle:
      print(-1)
  else:
      for i in range(2, n+1):
          if dist[i] == INF:
              print(-1)
          else:
              print(dist[i])
  
  ```
  
[출처] 
https://jina-developer.tistory.com/118
https://freedeveloper.tistory.com/277