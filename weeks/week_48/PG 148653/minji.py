'''
자리수가 6~9인 경우는 큰값
자리수가 1~4인 경우는 작은 값
5인 경우는 다음 자리수에 따라 달라짐
'''


def solution(storey):
    answer = 0

    while storey:
        tmp = storey % 10

        if tmp > 5:
            answer += (10 - tmp)
            storey += 10
        elif tmp < 5:
            answer += tmp
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += (10 - tmp)
        storey //= 10
    return answer