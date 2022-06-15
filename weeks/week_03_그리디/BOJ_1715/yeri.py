import sys
import heapq
input = sys.stdin.readline
N=int(input())
cards=[]
for _ in range(N):
    heapq.heappush(cards,int(input())) # 최소 힙을 통해 정렬
time=0
while len(cards)!=1:
    compared=heapq.heappop(cards)+heapq.heappop(cards) # 가장 작은 두 개를 섞음
    time+=(compared)
    heapq.heappush(cards,compared) # 섞은 것을 heappush를 통해 다른 것과의 비교가 진행되도록
print(time)
# 항상 가장 작은 두 카드 묶음을 꺼내야 하니 새로 더한 것도 비교군에 넣어야 한다.