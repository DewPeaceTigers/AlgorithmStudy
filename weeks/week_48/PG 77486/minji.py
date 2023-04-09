from collections import defaultdict
import math


def solution(enroll, referral, seller, amount):
    answer = []
    result = defaultdict(int)
    n = len(enroll)
    graph = defaultdict(str)

    # 트리구조 만들기
    for i in range(n):
        if referral[i] == "-":
            continue
        else:
            graph[enroll[i]] = referral[i]
    # print(graph)

    for i in range(len(seller)):
        profit = amount[i] * 100
        result[seller[i]] += math.ceil(profit * 0.9)
        reminder = math.floor(profit * 0.1)

        # 수익 분배 계산
        now = graph[seller[i]]
        while now:
            result[now] += math.ceil(reminder * 0.9)
            reminder = math.floor(reminder * 0.1)
            now = graph[now]
            if reminder == 0:  # 더이상 분배금이 없으면 종료
                break

    for i in range(n):
        answer.append(result[enroll[i]])

    return answer