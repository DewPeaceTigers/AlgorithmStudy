'''
1. course의 단품 개수만큼 order별로 조합구하기
2. 해당 조합을 주문한 횟수 count
3. 최댓값을 갖는 조합 answer에 저장
'''
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for c in course :
        comb=[]
        for order in orders :
            comb+=combinations(sorted(order), c) #order애서 개수만큼
        counter=Counter(comb) #딕셔너리 형태로 변환 Key는 조합 value는 개수

        if len(counter)>0 and max(counter.values())!=1 : #2번 이상 주문
            answer+=(''.join(k) for k,v in counter.items() if max(counter.values()) == v)

    return sorted(answer)