from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    answer = []

    # course_menu[i] : 단품메뉴 i개로 구성된 모든 코스요리 정보
    # course_menu[i] = { 메뉴구성1: 주문횟수1, 메뉴구성2: 주문횟수2...}
    course_menu = [defaultdict(int) for _ in range(11)]

    for i in course:
        for order in orders:
            menu = list(order)
            menu.sort()

            # i개로 구성된 코스요리
            for case in combinations(menu, i):
                m = "".join(case)
                course_menu[i][m] += 1

        # 단품메뉴 i개로 구성된 코스요리 중 주문횟수 최댓값 구하기
        max_cnt = 0
        if course_menu[i].values():
            max_cnt = max(course_menu[i].values())

        # 최대 주문횟수가 2보다 작은 경우 넘어감
        if max_cnt < 2:
            continue

        # 최대 주문횟수에 해당하는 코스요리 추가
        for menu, cnt in course_menu[i].items():
            if cnt == max_cnt:
                answer.append(menu)

    answer.sort()

    return answer
