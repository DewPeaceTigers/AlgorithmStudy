def solution(play_time, adv_time, logs):
    answer = ''

    # play_time을 초 단위로 변환
    h, m, s = map(int, play_time.split(":"))
    N = (h*3600)+(m*60)+s

    # 특정 시간에 재생된 곡수 저장
    play = [0]*(N+1)

    for log in logs:
        time = log.split("-")
        s = list(map(int, time[0].split(":")))
        e = list(map(int, time[1].split(":")))

        start = s[0]*3600+s[1]*60+s[2]
        end = e[0]*3600+e[1]*60+e[2]

        # 시작시간 +1, 종료시간 -1
        play[start] += 1
        play[end] -= 1

    # 누적합 이용
    # play[x] : 시각 x부터 x+1까지 1초 간의 구간을 포함하는 재생 구간의 개수
    for i in range(N-1):
        play[i+1] += play[i]

    # 누적합 한번더
    # play[x] : 시각 0부터 x+1까지 x+1초 간의 구간을 포함하는 누적 재생시간
    for i in range(N-1):
        play[i+1] += play[i]

    # 공익광고 재생 구간 길이
    ad = list(map(int, adv_time.split(":")))
    adv = ad[0]*3600 + ad[1]*60+ad[2]

    # 누적 재생시간 최댓값 저장
    max_play = max(play[:adv])

    # 공익광고가 들어갈 시작 위치 저장
    adv_pos = 0

    for x in range(N-adv):
        # 구간 누적 재생시간 구하기
        sum_play = play[x+adv]-play[x]

        if sum_play > max_play:
            adv_pos = x+1  # 시작 시각 업데이트
            max_play = sum_play
            # print("갱신", adv_pos, adv_pos//3600, (adv_pos%3600)//60, adv_pos%60)

    # "시간:분:초" 형태로 변환
    answer = "{0:02d}:{1:02d}:{2:02d}".format(
        adv_pos//3600, (adv_pos % 3600)//60, adv_pos % 60)

    return answer
