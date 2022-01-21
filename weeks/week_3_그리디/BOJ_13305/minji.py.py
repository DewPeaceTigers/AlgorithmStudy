import sys
n=int(input())
km=list(map(int, sys.stdin.readline().split())) #거리
l=list(map(int, sys.stdin.readline().split())) #리터당 가격

cost = km[0]*l[0] #첫번째 도시에서 두번째 도시까지 가는 비용
min_cost = l[0] #첫번째 도시 기름 가격
for i in range(1, n-1) :
	if min_cost <= l[i] :
		cost += min_cost*km[i]
	else : #현재 위치한 도시 기름 가격이 더 싼 경우
		cost += l[i]*km[i]
		min_cost = l[i]
print(cost)