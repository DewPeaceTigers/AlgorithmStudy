from collections import deque

def solution(n, t, m, timetable):
    answer = ''
    timetable.sort()
    timetable=deque(timetable)
    for i in range(len(timetable)):
        hour,mins = map(int,timetable[i].split(":"))
        timetable[i] = hour*60+mins
    print(timetable)
    que = dict()
    now = 9*60
    for _ in range(n):
        que[now] = []
        now+=t
    idx = 0
    for time in que:
        while idx<len(timetable) and timetable[idx] <= time:
            if len(que[time])>=m: break
            que[time].append(timetable[idx])
            idx+=1
    print(que)
    for time in reversed(que):
        if 0<len(que[time])<m:
            last_person = que[time][-1]
            answer = str(last_person//60)+":"+str(last_person%60)
            break
    if answer =='':
        first = timetable[0]
        answer = str(first//60)+":"+str(first%60)
    return answer