import heapq


def solution(operations):
    heap = []

    for op in operations:
        order, num = op.split(" ")
        num = int(num)
        if order == "I":
            ## 입력
            heapq.heappush(heap, num)
        else:
            if not heap:
                continue
            ## 제거
            if num == 1:
                heap.remove(max(heap))
                heapq.heapify(heap) # 순서가 흐트러졌으니 다시 힙하기
            else:
                heapq.heappop(heap)
    if heap:
        return [max(heap), heapq.heappop(heap)]
    else:
        return [0, 0]