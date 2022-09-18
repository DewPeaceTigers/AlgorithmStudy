import heapq

def solution(jobs):
    answer = 0
    start, now, i=-1, 0, 0
    heap=[]
    while i<len(jobs) :
        for job in jobs :
            if start < job[0] <=now :
                heapq.heappush(heap, [job[1], job[0]])
        if len(heap)>0 :
            cur=heapq.heappop(heap)
            start=now
            now+=cur[0]
            answer+=(now-cur[1])
            i+=1
        else:
            now+=1
    return int(answer/len(jobs))