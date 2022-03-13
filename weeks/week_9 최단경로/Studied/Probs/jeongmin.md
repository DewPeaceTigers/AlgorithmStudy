## 정민

1. 다익스트라 알고리즘과 벨만포드 알고리즘의 차이점

2. 다익스트라 알고리즘에서 시간복잡도는?

3. 플로이드 워셜 알고리즘이 최단거리를 갱신할 때 사용하는 점화식은?

4. 다익스트라 알고리즘이 그리디 알고리즘으로 분류되는 이유

5. 벨만-포드 알고리즘의 구현 코드입니다. 빈칸을 채워주세요.

    ```python
    def bf(start):
        # 시작 노드에 대해서 초기화
        dist[start] = 0

        # 전체 n번의 라운드(round)를 반복
        for i in range(n):
            # 매 반복마다 '모든 간선'을 확인하며
            for cur in range(n):
                for (next_node, cost) in graph[cur]:
                    # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧을 경우
                    if _______________ and ___________________:
                        dist[next_node] = dist[cur] + cost

                        # 음수 순환이 존재하는 경우 판별
                        if ______________:
                            return True

        return False
    ```