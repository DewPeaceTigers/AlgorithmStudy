import heapq

def solution(book_time):
    answer = 0

    times = []
    heap = []
    for time in book_time:
        start = int(time[0][:2]) * 60 + int(time[0][3:])
        end = int(time[1][:2]) * 60 + int(time[1][3:]) + 10
        times.append([start, end])

    times.sort()

    for time in times:
        if len(heap) == 0:
            answer += 1
            heapq.heappush(heap, time[1])
            continue

        if heap[0] <= time[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, time[1])
        else:
            heapq.heappush(heap, time[1])
        print(heap)
    return len(heap)