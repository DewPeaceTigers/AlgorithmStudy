'''
시간초과

from collections import defaultdict
from itertools import combinations

def solution(weights) :
    weight_idx=defaultdict(list)
    pairs=set()

    for idx, weight in enumerate(weights) :
        weight_idx[weight*2].append(idx)
        weight_idx[weight*3].append(idx)
        weight_idx[weight*4].append(idx)

    for key, value in weight_idx.items() :
        if len(value)>=2 :
            for comb in combinations(value, 2) :
                pairs.add(comb)

    print(pairs)
    return len(pairs)
'''
from collections import Counter

def solution(weights) :
    answer=0
    c=Counter(weights)

    #1:1이 짝궁인 경우
    for key, value in c.items() :
        if value>=2 :
            answer+=value*(value-1)//2

    weights=set(weights) #중복 몸무게 제거

    #2:3, 2:4, 3:4 비율
    for weight in weights :
        if weight*2/3 in weights :
            answer+=c[weight*2/3] * c[weight]
        if weight*2/4 in weights:
            answer+=c[weight*2/4] * c[weight]
        if weight*3/4 in weights:
            answer+=c[weight*3/4] *c[weight]

    return answer