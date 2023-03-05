'''
q1의 합으로만 결과 찾기
매번 sum 함수를 돌리면 시간초과 발생 -> 큐의 합을 저장하는 변수 사용
'''

from collections import deque


def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)

    find_sum = (sum(queue1) + sum(queue2)) // 2
    sum_q1 = sum(queue1)

    while (q1 and q2):
        if (sum_q1 > find_sum):
            sum_q1 -= q1.popleft()
        elif sum_q1 < find_sum:
            q1.append(q2.popleft())
            sum_q1 += q1[-1]
        else:
            if (sum_q1 == find_sum):
                return answer
        answer += 1
    return -1