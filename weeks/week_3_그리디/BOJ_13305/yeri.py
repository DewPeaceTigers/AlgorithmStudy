import sys
input = sys.stdin.readline
N=int(input())
lines=list(map(int,input().split()))
cities=list(map(int,input().split()))

cost=0
recent_fuel=int(1e9) # min 개념 이용
for i in range(N-1):
    if recent_fuel > cities[i]: # 현재 값이 최근 구매 값보다 싸면 주유값 바꿔주고
        recent_fuel=cities[i]
    cost+=recent_fuel*lines[i] # 도시마다 이전의 값을 참고해서 주유 삼
print(cost)