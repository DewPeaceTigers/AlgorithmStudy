'''
동일한 가짓수의 토핑
'''
from collections import Counter


def solution(topping):
    answer = 0
    A_dict = {}
    B_dict = Counter(topping)

    if len(topping) == 1: return answer

    for i in range(len(topping)):
        if B_dict[topping[i]] > 1:
            B_dict[topping[i]] -= 1
        elif B_dict[topping[i]] == 1:
            del B_dict[topping[i]]
        A_dict[topping[i]] = A_dict.get(topping[i], 0) + 1
        if len(B_dict) == len(A_dict):
            answer += 1

    return answer