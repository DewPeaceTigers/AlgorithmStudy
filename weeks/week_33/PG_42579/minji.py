from collections import defaultdict


def solution(genres, plays):
    answer = []
    genre_dicts = defaultdict(int)
    genre_arr = []
    for i in range(len(genres)):
        genre_dicts[genres[i]] += plays[i]  # 총 count
        genre_arr.append([genres[i], plays[i], i])

    genre_arr.sort(key=lambda x: (x[0], -x[1], x[2]))  # 장르별->count->index 순으로 정렬
    genre_dicts = sorted(genre_dicts.items(), key=lambda x: -x[1])  # 총 재생횟수가 큰 순

    for genre_dict in genre_dicts:
        # print(genre_dict[0])
        count = 0
        for genre in genre_arr:
            if genre_dict[0] == genre[0]:
                count += 1
                if count > 2:
                    break
                else:
                    answer.append(genre[2])

    return answer