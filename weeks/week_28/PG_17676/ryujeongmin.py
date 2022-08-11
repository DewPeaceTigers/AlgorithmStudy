""" 풀이 참고.. """


def solution(lines):
    answer = 0
    log = [] # log의 (시작시간, 끝시간) 저장

    for line in lines:
        date, s, t = line.split() # 날짜, 응답완료시간, 처리시간
        s = s.split(':')
        t = t.replace('s', '')

        # 끝시간을 msec 단위로 저장
        end = (int(s[0])*3600 + int(s[1])*60 + float(s[2])) * 1000 
        # 시작 시간을 msec 단위로 저장
        start = end - float(t)*1000 + 1 
        log.append([start, end])

    for x in log:
    	# 최대 초당 처리량 구하기
        answer = max(answer, throughput(log, x[0], x[0] + 1000), throughput(log, x[1], x[1] + 1000))

    return answer

# 초당 처리량을 구하는 함수
def throughput(log, start, end):
    cnt = 0
    for x in log:
        if x[0] < end and x[1] >= start:
            cnt += 1
    return cnt