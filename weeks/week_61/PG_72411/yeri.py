
from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []
    for n in course:
        result = defaultdict(int)
        for order in orders:
            order = sorted(list(order))
            for c in combinations(order,n):
                result[''.join(c)]+=1
        if result:
            result_list = list(result.items())
            result_list.sort(key=lambda x:-x[1])
            max_num = result_list[0][1]
            if max_num !=1:
                for menu, num in result_list:
                    if max_num > num: break
                    answer.append(menu)
    return sorted(answer)