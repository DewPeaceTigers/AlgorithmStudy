def solution(queue1, queue2):
    answer = -2

    sum1 = sum(queue1)
    sum2 = sum(queue2)
    target = (sum1 + sum2)//2

    # 투 포인터 사용하기
    p1, p2 = 0, len(queue1)

    q = queue1 + queue2

    # 움직인 횟수
    cnt = 0
    while sum1 != target:
        # 불가능한 경우
        if p1 > p2 or p2 >= len(q):
            cnt = -1
            break

        # 값이 더 작다면 우측 포인터 오른쪽으로
        if sum1 > target:
            sum1 -= q[p1]
            p1 += 1

        # 값이 더 크다면 좌측 포인터 왼쪽으로
        else:
            sum1 += q[p2]
            p2 += 1

        cnt += 1

    answer = cnt

    return answer
