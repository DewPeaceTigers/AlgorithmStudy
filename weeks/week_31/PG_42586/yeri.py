
from collections import deque
import math
def solution(progresses, speeds):
    days = [ math.ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))]
    answer = []
    while days:
        day = days[0]
        cnt = 1
        for d in range(1,len(days)):
            if day >= days[d]:
                cnt+=1
            else:
                break
        answer.append(cnt)
        days = days[cnt:]
    return answer