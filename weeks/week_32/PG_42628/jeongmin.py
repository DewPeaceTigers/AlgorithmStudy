import heapq

def solution(operations):
    answer = []
    
    maxHeap = []    # 최소힙
    minHeap = []    # 최대힙
    
    for operation in operations:
        op, x = operation.split(" ")

        if op=='I':
            heapq.heappush(maxHeap, -int(x))
            heapq.heappush(minHeap, int(x))
        else:
            if len(maxHeap)==0:
                continue
                
            if x=='1':
                minHeap.remove(-heapq.heappop(maxHeap))
            else:
                maxHeap.remove(-heapq.heappop(minHeap))

    if len(maxHeap)==0:
        answer = [0, 0]
    else:
        answer = [-heapq.heappop(maxHeap), heapq.heappop(minHeap)]
    
    return answer