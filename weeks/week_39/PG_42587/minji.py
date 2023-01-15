def solution(priorities, location):
    answer=0
    queue=[[idx, priority] for idx, priority in enumerate(priorities)]

    while True :
        cur=queue.pop(0)
        for idx, priority in queue :
            if cur[1]<priority :
                queue.append(cur)
            else:
                answer+=1
                if(cur[0]==location) : return answer
    return answer