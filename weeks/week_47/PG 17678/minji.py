'''
각 시간별로 탑승하는 크루 계산
버스에 자리가 있으면 마지막으로 탑승
버스에 탈 자리가 없으면 마지막 크루 탑승보다 1분 먼저
'''


def solution(n, t, m, timetable):
    answer = 0
    timetable = [int(time[:2]) * 60 + int(time[3:]) for time in timetable]  # 버스 시간 분 단위로 계산
    timetable.sort()

    bus_time = [9 * 60 + t * i for i in range(n)]

    idx = 0
    for time in bus_time:
        cnt = 0
        while cnt < m and idx < len(timetable) and timetable[idx] <= time:
            cnt += 1
            idx += 1
        if cnt < m:  # 버스에 자리 있는 경우
            answer = time
        else:
            answer = timetable[idx - 1] - 1

    return str(answer // 60).zfill(2) + ":" + str(answer % 60).zfill(2)