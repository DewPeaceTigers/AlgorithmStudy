from collections import defaultdict
def solution(genres, plays):
    answer = []
    dic = defaultdict(list) # 장르별 곡 번호, 재생횟수 저장
    dic_total = defaultdict(int) # 장르별 총 재생횟수 저장
    for i in range(len(genres)):
        dic[genres[i]].append((i,plays[i]))
        dic_total[genres[i]]+=plays[i]

    dic_total = list(dic_total.items()) 
    dic_total.sort(key=lambda x:-x[1]) # 재생횟수 큰 순으로 정렬

    for genre, _ in dic_total:
        # 큰 재생횟수의 장르부터 뽑아서
        dic[genre].sort(key=lambda x:(-x[1],x[0])) # 각 곡에 대해 정렬 후
        limit = 0
        for n, _ in dic[genre]: # 2개씩만 수록
            if limit == 2: break
            answer.append(n)
            limit +=1
    return answer