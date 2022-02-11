import sys
import heapq
input=sys.stdin.readline
N=int(input())

front,back=[],[]
for i in range(1,N+1):
    one = int(input())
    if i==1:
        heapq.heappush(front,-one)
        print(-front[0])
    elif i%2!=0:
        # 홀수: 앞 배열 맨 뒤
        heapq.heappush(front,-one)
        if -front[0]>back[0]: # 양 힙의 루트 정렬해주기
            f=-heapq.heappop(front)
            b=heapq.heappop(back)
            heapq.heappush(front,-b)
            heapq.heappush(back,f)
        print(-front[0])
    else:
        # 짝수: 양 배열 개수 동일하게 맞추기, 앞 배열 맨 뒤와 뒷 배열 맨 앞 비교
        if -front[0]>=one: # front의 루트가 새로 들어오는 것보다 크거나 같다면 (새로 들어온 것이 작은 것)
            heapq.heappush(front,-one)
        else:
            heapq.heappush(back,one)
            
        if len(front)>len(back): # 개수 맞추기
            move=-heapq.heappop(front)
            heapq.heappush(back,move)
        elif len(front)<len(back):
            move=heapq.heappop(back)
            heapq.heappush(front,move)
        print(min(-front[0],back[0]))