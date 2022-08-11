def solution(lines):
    times = []
    logs = []
    for line in lines:
        _, datetime, length = line.split(' ')
        h,m,s_ = datetime.split(':')
        s, ss = s_.split('.')
        l = length.replace('s',' ')
        end = (int(h)*60*60+int(m)*60+float(s_))*1000
        start = end - (float(l)*1000-1)
        times.append(start)
        times.append(end)
        logs.append([start,end])
    times.sort()
    # 시작시간과 종료시간 기준으로 탐색 시작 <- 처리 작업의 개수가 변하는 경우는 시작시간과 종료시간밖에 없다.. ⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️
    logs.sort(key=lambda x:x[0])
    maxCnt = 0
    for time in times:
        left = time
        right = time+999 # 1000ms
        cnt = 0 # 해당 구간 log 세기
        for start, end in logs:
            if left <= start <= right:
                cnt+=1
            elif left<= end <= right:
                cnt+=1
            elif start<= left and right <= end:
                cnt+=1
        maxCnt = max(cnt,maxCnt)
    return maxCnt