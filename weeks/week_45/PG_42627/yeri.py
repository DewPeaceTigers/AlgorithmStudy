import heapq
from collections import deque
import math
def solution(jobs):
    answer = 0
    jobs.sort()
    cands = [] 
    done = 0
    idx = 0
    end =0
    while done< len(jobs):
        for i in range(idx,len(jobs)):
            if jobs[i][0] <= end:
                heapq.heappush(cands,[jobs[i][1],jobs[i][0]])
                idx+=1
            else: break
        if not cands:
            end = jobs[idx][0]
            continue
        l,a = heapq.heappop(cands)
        answer += end+l-a
        end += l
        done+=1
    return answer//len(jobs)