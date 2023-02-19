import heapq

def solution(genres, plays):
    answer = []
    
    # 노래 개수
    N = len(plays)
    
    # 장르별 재생횟수 저장
    genres_cnt = {g:0 for g in set(genres)}
    # 장르별 노래 정보 저장 [재생횟수, 고유번호]
    genres_detail = {g:[] for g in set(genres)}
    
    for i in range(N):
        genre, play = genres[i], plays[i]
        
        # 장르별 재생횟수 저장
        genres_cnt[genre] += play
    
        # 장르 별 가장 많이 재생된 노래 두 개씩 저장
        if len(genres_detail[genre]) < 2:
            # 노래가 두 개 미만인 경우는 그대로 추가
            heapq.heappush(genres_detail[genre], [play, -i])
        else:
            play_cnt, num = genres_detail[genre][0]
            # 재생 횟수가 더 많거나, 재생 횟수가 같은데 고유 번호가 낮은 노래인 경우
            heapq.heappushpop(genres_detail[genre], [play, -i])
    
    # 속한 노래가 많이 재생된 장르 순으로 정렬
    genres_cnt = list(genres_cnt.items())
    genres_cnt.sort(key=lambda x:-x[1])

    for genre, cnt in genres_cnt:
        songs = genres_detail[genre][::-1]

        # 장르 내에서 많이 재생된 순으로 저장
        for song in songs:
            answer.append(-song[1])
        
    return answer