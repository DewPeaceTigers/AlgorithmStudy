def change(music) :
    if 'A#' in music :
        music=music.replace('A#', 'a')
    if 'C#' in music :
        music=music.replace('C#', 'c')
    if 'D#' in music :
        music=music.replace('D#', 'd')
    if 'F#' in music :
        music=music.replace('F#', 'f')
    if 'G#' in music:
        music=music.replace('G#', 'g')
    return music
def solution(m, musicinfos):
    answer = ''
    music_list=[]
    m_len=len(m)
    m=change(m)
    index=0
    for musicinfo in musicinfos :
        index+=1
        info=musicinfo.split(',')
        start=info[0].split(':')
        end=info[1].split(':')
        time=(int(end[0])-int(start[0]))*60+(int(end[1])-int(start[1])) #재생시간
        music=change(info[3]) #소문자로 변경
        music=music*(time//len(music))+music[:time%len(music)]
        if m in music : #재생 시간, 순서, 노래 제목 저장
            music_list.append([time, index, info[2]])
    if not music_list:
        answer='(None)'
    elif len(music_list)==1 :
        answer=music_list[0][2]
    else:
        music_list.sort(key=lambda x:(-x[0], x[1]))
        answer=music_list[0][2]
    return answer
