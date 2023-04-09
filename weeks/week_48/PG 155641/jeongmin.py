# 누적합 사용하기!

def solution(book_time):
    answer = 0

    room = [0] * (24*60+10)

    # 시간을 분으로 변환
    for time in book_time:
        # 입실시간 +1 처리
        h, m = map(int, time[0].split(":"))
        room[h*60+m] += 1

        # 퇴실시간 -1 처리
        out_h, out_m = map(int, time[1].split(":"))
        room[out_h*60+out_m+10] -= 1

    # 누적합 구하기
    for i in range(1, 24*60+10):
        room[i] = room[i]+room[i-1]

    answer = max(room)

    return answer
