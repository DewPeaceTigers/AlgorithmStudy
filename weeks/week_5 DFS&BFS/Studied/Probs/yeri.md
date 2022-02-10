## 예리

1. DFS와 BFS의 차이점은?
2. DFS와 BFS의 시간 복잡도에 대해 설명하세요.
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

4. 최단 거리를 구하는 문제에 적합한 것은 BFS이다. 답은 O/X로 표시하고, 이유를 설명하세요.
5. DFS와 BFS는 대표적 '**\_\_**' 탐색 알고리즘이다.
