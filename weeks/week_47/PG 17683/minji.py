'''
# 치환 X
# 19번만 안됨,,,
import re

def play_time(start, end):
    s_h, s_m = map(int, start.split(":"))
    e_h, e_m = map(int, end.split(":"))

    return (e_h - s_h) * 60 + (e_m - s_m)


def solution(m, musicinfos):
    answer = ''
    answer_time = 0
    for music in musicinfos:
        music = music.split(",")

        time = play_time(music[0], music[1])  # 재생 시간
        # #이 포함된 횟수만큼 더 반복
        cnt_shape = music[3].count("#")
        music_info = music[3]
        if len(music[3]) - cnt_shape < time:  # 재생 시간 만큼 반복
            music_info = music_info * (time // (len(music[3]) - cnt_shape)) + music_info[
                                                                              :time % (len(music[3]) - cnt_shape)]
        else:
            music_info = music_info[:time + cnt_shape]
        print(music_info)

        for text in re.finditer(m, music_info):  # 여러 문자열 찾기
            print(text.start())
            if m[-1] != "#" and len(music_info) > text.start() + len(m) and music_info[
                text.start() + len(m)] == "#":  # C와 C#구분
                continue
            if answer_time <= time:
                answer = music[2]
                answer_time = time
                break

    if len(answer) == 0:
        return "(None)"
    return answer
'''


def play_time(start, end):
    s_h, s_m = map(int, start.split(":"))
    e_h, e_m = map(int, end.split(":"))

    return (e_h - s_h) * 60 + (e_m - s_m)


def solution(m, musicinfos):
    answer = ''
    answer_time = 0
    change = {'C#': 'c', 'D#': 'd', 'F#': 'f', 'G#': 'g', 'A#': 'a'}

    for key, value in change.items():
        m = m.replace(key, value)

    for music in musicinfos:
        music = music.split(",")

        time = play_time(music[0], music[1])  # 재생 시간
        music_info = music[3]
        for key, value in change.items():
            music_info = music_info.replace(key, value)

        if len(music_info) < time:  # 재생 시간 만큼 반복
            music_info = music_info * (time // len(music_info)) + music_info[:time % len(music_info)]
        else:
            music_info = music_info[:time]
        # print(music_info)

        if m in music_info and answer_time < time:
            answer = music[2]
            answer_time = time

    if len(answer) == 0:
        return "(None)"
    return answer