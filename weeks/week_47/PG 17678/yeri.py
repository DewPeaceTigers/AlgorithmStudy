from collections import deque

def solution(n, t, m, timetable):
    answer = ''
    timetable.sort()
    timetable=deque(timetable)
    for idx in range(len(timetable)):
        hour,mins = map(int,timetable[idx].split(":"))
        timetable[idx] = hour*60+mins
    que = dict() 
    now = 9*60
    for _ in range(n):
        que[now] = []
        now+=t
    wait = 0
    for time in que:
        while wait<len(timetable) and timetable[wait] <= time:
            if len(que[time])<m:
                que[time].append(timetable[wait])
                wait+=1
            else: break
    last = list(que)[-1]
    if 0<=len(que[last])<m:
        answer = last
    elif len(que[last])>=m:
        answer = que[last][-1]-1 
    hh = answer//60
    mm = answer%60
    return '{0:0>2}'.format(hh)+':{0:0>2}'.format(mm)