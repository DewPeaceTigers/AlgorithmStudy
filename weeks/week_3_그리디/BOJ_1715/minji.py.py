'''
group : 카드 묶음 수
paper : 카드 개수
'''
import sys
import heapq

group = int(input())
paper = [int(sys.stdin.readline()) for x in range(group)]
paper.sort()

if group == 1 :#묶음이 하나인 경우는 비교 필요 없음
    print(0)
else :
    count = 0
    heapq.heapify(paper)
    while len(paper)>1:
        a, b = heapq.heappop(paper), heapq.heappop(paper)
        count+=a+b
        heapq.heappush(paper, a+b)
    print(count)
