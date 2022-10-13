"""
장르별로 가장 많이 재생된 노래를 최대 두 개까지 모아 베스트 앨범 출시
"""
from collections import defaultdict
import heapq

def solution(genres, plays):
    answer = []
    
    album = defaultdict(list)  # 장르, 노래별 재생 수 저장
    pcnt = defaultdict(int)   # 장르에 속한 노래들 재생 수 저장
    
    for i, genre in enumerate(genres):
        pcnt[genre] += plays[i]

        # 큐에 원소 1개 이하 일때는 무조건 큐에 넣기
        if len(album[genre])<=1:
            heapq.heappush(album[genre], [plays[i], i])

        # 더 많이 재생된 노래일 경우 큐에 넣기
        elif plays[i] > album[genre][0][0]:
            heapq.heappop(album[genre])
            heapq.heappush(album[genre], [plays[i], i])

    # 속한 노래가 많이 재생된 장르 순으로 정렬
    sg = sorted(pcnt.items(), key=lambda x: -x[1])
    
    for genre, cnt in sg:
        # 장르 내에서 많이 재생된 노래 순 
        # 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 순
        sl = sorted(album[genre], key=lambda x: [-x[0], x[1]])
        # print(sl)
        for play, idx in sl:
            answer.append(idx)
    
    return answer