"""
- 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.
- 모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하는 프로그램을 작성하시오.
위 조건들을 유념해야 한다..!
그래프는 방향 그래프이고, 노선이 중복될 수 있기에 작은 것을 넣어둬야한다..!
"""
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
INF= n*100000+1 # 노드 * 간선 최대 값 + 1
graph=[[INF]*n for _ in range(n)]
for i in range(n):
    graph[i][i]=0
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a-1][b-1]=min(graph[a-1][b-1],c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j]=min(graph[i][j], graph[i][k]+graph[k][j])
            
for i in range(n):
    for j in range(n):
        if graph[i][j]==INF: print(0, end=' ')
        else: print(graph[i][j],end=' ')
    print()