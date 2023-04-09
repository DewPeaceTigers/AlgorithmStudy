import heapq
def getTime(time):
    h,m = map(int,time.split(":"))
    return h*60+m
def solution(book_time):
    answer = 0
    peop = []
    rooms = [-10]
    for start,end in book_time:
        start = getTime(start)
        end = getTime(end)
        heapq.heappush(peop,(start,end))
    while peop:
        start,end = heapq.heappop(peop)
        if rooms[0]+10 <= start:
            heapq.heappop(rooms)
        heapq.heappush(rooms,end)
    return len(rooms)