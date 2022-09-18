import heapq
def solution(jobs):
    answer = 0
    jobs.sort()
    wait = []
    # heapq.heappush(wait,[jobs[0][1],jobs[0][0]])
    cur = 0
    idx = 0
    done = 0
    while done<len(jobs):
        for i in range(idx,len(jobs)):
            if jobs[i][0] <= cur:
                # 끝난 시간 전에 도착한 것들
                heapq.heappush(wait,[jobs[i][1],jobs[i][0]])
                idx+=1
            else: break
        if not wait:
            cur = jobs[idx][0]
            continue
        need, arrived = heapq.heappop(wait)
        answer += cur+need-arrived # 대기 시간
        cur += need # 끝난 시간
        done+=1
    return answer//len(jobs)