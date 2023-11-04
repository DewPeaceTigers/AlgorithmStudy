from collections import defaultdict,deque
N, M = map(int,input().split())
# 위상 정렬
# 사이클이 없는 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것을 의미
# 순서가 있어서 진입차수를 고려하는 알고리즘

# 큐를 이용하는 위상 정렬 알고리즘의 동작 과정은 다음과 같다
# 진입차수가 0인 모든 노드를 큐에 넣는다
# 큐가 빌 때까지 다음의 과정을 반복한다
# 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거한다
# 새롭게 진입차수가 0이 된 노드를 큐에 넣는다
# => 결과 적으로 각 노드가 큐에 들어온 순서가 위상 정렬을 수행한 결과와 같다

dict = defaultdict(list)
init = [0]*N
for _ in range(M):
    f,b = map(int,input().split())
    dict[f-1].append(b-1)
    init[b-1]+=1

q = deque()
for i in range(N):
    if init[i]==0:
        q.append(i)
route=[]
while q:
    f = q.popleft()
    route.append(f)

    for n in dict[f]:
        init[n] -=1
        if init[n]==0:
            q.append(n)

for r in route : print(r+1,end=" ")