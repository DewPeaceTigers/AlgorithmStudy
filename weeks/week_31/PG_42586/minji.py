import math

def solution(progresses, speeds):
    times = []
    answer = []
    for i in range(len(progresses)):
        times.append(math.ceil((100 - progresses[i]) / speeds[i]))

    before = times[0]
    count = 1
    for i in range(1, len(times)):
        if before >= times[i]:
            count += 1
        else:
            before = times[i]
            answer.append(count)
            count = 1
    if count > 0:
        answer.append(count)
    return answer