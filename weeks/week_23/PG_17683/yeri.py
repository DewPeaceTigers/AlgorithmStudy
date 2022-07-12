def switch(music):
    record=''
    for i in range(len(music)):
        if music[i]=='#': continue
        if i+1<len(music) and music[i+1] =='#':
            record+=music[i].lower()
        else:
            record+=music[i]
    return record
def solution(m, musicinfos):
    answer = ''
    m = switch(m)
    longest=0
    for musicinfo in musicinfos:
        infos = musicinfo.split(',')
        start = list(map(int,infos[0].split(':')))
        end = list(map(int,infos[1].split(':')))
        time = (end[0]*60+end[1])-(start[0]*60+start[1])
        if len(m)<=time:
            # 재생 시간보다 길다면 아님
            # 짧은거만 확인
            song = switch(infos[3])
            if len(song)<time:
                for i in range(time-len(song)):
                    song+=song[i%len(song)]
            else:
                 song= song[:time]
            if m in song and longest < time:
                answer=infos[2]
                longest = time
    if not answer:
        answer="(None)"
    return answer