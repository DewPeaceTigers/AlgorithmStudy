from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []
    for o in range(len(orders)):
        orders[o]=''.join(list(sorted(orders[o])))
    for c in course:
        c_set=defaultdict(int)
        for order in orders:
            for cb in combinations(order,c):
                c_set[''.join(cb)]+=1
        mx_cnt = 2
        mx_combs = []
        for key,cnt in c_set.items():
            if mx_cnt < cnt:
                mx_cnt =cnt
                mx_combs=[key]
            elif mx_cnt==cnt:
                mx_combs.append(key)
        answer.extend(mx_combs)
    return sorted(answer)