import heapq


def solution(operations):
    answer = []
    heap = []
    max_heap = []

    for operation in operations:
        op, num = operation.split()
        num = int(num)
        if op == "I":
            heapq.heappush(heap, num)
            heapq.heappush(max_heap, (num * (-1), num))
        elif op == "D":
            if len(heap) > 0:
                if num == 1:
                    max_num = heapq.heappop(max_heap)[1]
                    heap.remove(max_num)
                else:
                    min_num = heapq.heappop(heap)
                    max_heap.remove((min_num * (-1), min_num))

    if len(heap) > 0:
        return [heapq.heappop(max_heap)[1], heapq.heappop(heap)]

    return [0, 0]