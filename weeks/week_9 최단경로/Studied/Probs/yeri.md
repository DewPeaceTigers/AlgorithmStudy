## 예리

1. 다익스트라 알고리즘은 시작 노드에서 모든 노드까지의 거리를 구하는 최단 경로 알고리즘이다. (O/X)

2. 플로이드 알고리즘의 시간 복잡도는?

3. 다익스트라 알고리즘과 벨만포드 알고리즘의 차이는?

4. 플로이드 알고리즘 코드이다. 빈칸을 채우세요

```python
import sys

INF = int(1e9)
n = int(input())
m = int(input())
# 2차원 거리테이블 리스트 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]
# 자신의 노드간의 거리는 0으로 변경
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0
# 주어지는 그래프 정보 입력
for _ in range(m):
    # a -> b로 가는 비용은 c
    a, b, c = map(int, input().split())
    graph[a][b] = c

# k=거쳐가는 노드
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min('__________________')
```

5. 다익스트라 알고리즘의 동작 방법을 설명하시오
