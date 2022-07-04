import heapq

def solution(m, musicinfos):
    answer = ''
    
    # C#, D#, F#, G#, A# => V, W, X, Y, Z
    change = {'C#':'V', 'D#':'W','F#':'X', 'G#':'Y', 'A#':'Z'}
    for key in change.keys():
        m = m.replace(key, change[key])
    
    heap = []
    for i, music in enumerate(musicinfos):
        start, end, name, melody = music.split(',')
        
        # C#, D#, F#, G#, A# => V, W, X, Y, Z
        for key in change.keys():
            melody = melody.replace(key, change[key])
            
        # 재생시간 구하기
        play_time = int(end[:2])*60+int(end[3:])-int(start[:2])*60-int(start[3:])
        
        # 힙 사용 (1.재생시간 내림차순 2.입력 오름차순) 
        heapq.heappush(heap, [-play_time, i, melody, name])
        
    t = 0
    match = []  # 조건이 일치하는 음악 리스트 저장
    while heap:
        time, i, melody, name = heapq.heappop(heap)
            
        # 조건이 일치하는 음악의 재생 길이보다 더 짧은 경우 break
        if t > -time:
            break
            
        l = len(melody)
        # 재생시간 만큼 재생된 음 리스트
        play = (melody*(-time//l+1))[:-time]
        
        if m in play:
            t = -time   # 재생시간 저장
            heapq.heappush(match, (i, name))
    
    # 조건이 일치하는 음악이 있을 때
    if match:
        answer = heapq.heappop(match)[1]
    # 조건이 일치하는 음악이 없을 때
    else:
        answer = "(None)"
        
    return answer