import heapq

def solution(scoville, K):
    # 섞은 횟수
    answer = 0
    
    # 최소힙 사용
    minHeap = scoville
    heapq.heapify(scoville)
    
    while True:
        size = len(minHeap)
        
        # 가장 작은값
        first = heapq.heappop(minHeap)
        
        # 길이가 1인 경우
        if size == 1:
            if first < K : answer = -1
            break
        
        # 최소값이 K이상인 경우
        if first >= K:
            break
        
        # 두번째로 작은값
        second = heapq.heappop(minHeap)
        
        # 섞은 음식의 스코빌 지수
        x = first + second*2
        heapq.heappush(minHeap, x)
        
        # 섞은 횟수 증가
        answer += 1    
    
    return answer