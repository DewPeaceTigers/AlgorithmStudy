from collections import defaultdict
def solution(genres, plays):
    answer = []
    genre = defaultdict(int)
    music = defaultdict(list)
    for i in range(len(genres)):
        genre[genres[i]]+=plays[i]
        music[genres[i]].append((plays[i],i))
    genre_list = list(genre.items())
    genre_list.sort(key=lambda x:-x[1])
    for type, cnt in genre_list:
        music[type].sort(key=lambda x:(-x[0],x[1]))
        for i in range(min(2,len(music[type]))):
            answer.append(music[type][i][1])
    return answer