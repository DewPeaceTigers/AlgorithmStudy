from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []

    for num in course:
        array = []
        for order in orders:
            order = sorted(order)
            array.extend(list(combinations(order, num)))

        count = Counter(array)

        if count:
            # 제일 많이 나온 조합이 두번 이상 시켜졌다면
            if max(count.values()) >= 2:
                for key, value in count.items():
                    # 현재 조합이 가장 많이 시켜졌다면 결과배열에 추가
                    if value == max(count.values()):
                        answer.append("".join(key))

    return sorted(answer)