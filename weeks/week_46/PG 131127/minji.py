from collections import Counter

def solution(want, number, discount):
    answer = 0
    buy_item = {}

    for i in range(len(want)):
        buy_item[want[i]] = number[i]
    for i in range(len(discount) - 9):
        if buy_item == Counter(discount[i:i + 10]):
            answer += 1
    return answer