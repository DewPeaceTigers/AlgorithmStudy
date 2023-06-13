def solution(k, ranges):
    answer = []
    y = [k]

    # y좌표 구하기
    while k > 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        y.append(k)
    cnt = len(y) - 1

    # 넓이 구하기
    areas = [(y[i] + y[i + 1]) / 2 for i in range(cnt)]

    for r in ranges:
        if r[0] - r[1] == cnt:
            answer.append(0.0)
        elif r[0] - r[1] > cnt:
            answer.append(-1.0)
        else:
            answer.append(sum(areas[r[0]:r[1] + cnt]))

    return answer