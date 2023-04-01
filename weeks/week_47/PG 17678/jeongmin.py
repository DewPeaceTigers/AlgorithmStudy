def solution(n, t, m, timetable):
    answer = ''

    # 도착시간을 분으로 변환
    timetable = [int(x[:2])*60 + int(x[3:]) for x in timetable]
    # 도착한 시간 순으로 정렬
    timetable.sort()  

    # 버스 시간
    bus = [9*60 + t*i for i in range(n)]

    idx = 0
    for time in bus:
        cnt = 0
        while cnt < m and idx < len(timetable) and timetable[idx] <= time:
            idx += 1
            cnt += 1

        # 버스에 자리가 남은 경우
        if cnt < m:
            answer = time
        else:
            # 버스 자리가 없는 경우 마지막 크루보다 전에 도착!
            answer = timetable[idx-1] - 1

    hour = str(answer // 60).zfill(2)
    minute = str(answer % 60).zfill(2)

    answer = hour + ":" + minute

    return answer