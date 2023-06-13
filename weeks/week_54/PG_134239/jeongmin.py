"""
(0, K), (1, y1), (2, y2), (3, y3), (4, y4) 일때

[0, 0] 구간에 대해 정적분한다면
    (1/2)*K + y1+y2+y3+ (1/2)*y4
    
=> 첫번째, 마지막 원소만 2로 나눈값을 더하고 나머지 중간 원소들 더해주기
"""


def solution(k, ranges):
    answer = []

    num = k

    # 누적합 배열
    sub_sum = [k]
    idx = 0
    while num != 1:
        # 짝수면 2로 나누기
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1

        # 누적합 저장
        sub_sum.append(sub_sum[idx] + num)
        idx += 1

    # 총 x좌표 개수
    N = len(sub_sum)

    for r in ranges:
        # 정적분을 하는 구간의 시작, 끝
        start, end = r[0], N-1 + r[1]

        # 유효하지 않은 구간일 경우
        if start > end:
            answer.append(-1)
            continue

        # 시작점, 끝점이 같다면
        if start == end:
            answer.append(0)
            continue

        # 첫번째 원소값
        first = sub_sum[start] - (sub_sum[start-1] if start > 0 else 0)

        # 중간 원소들의 합
        middle = sub_sum[end-1]-sub_sum[start]

        # 마지막 원소값
        last = sub_sum[end] - sub_sum[end-1]

        result = 1/2*first + middle + 1/2*last

        answer.append(result)

    return answer
