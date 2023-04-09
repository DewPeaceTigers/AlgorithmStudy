cnt = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1]
answer = 1e9


def magic(num, x):
    global answer

    if num < 10:
        # 5보다 크다면 올림 처리
        tmp = 1 if num > 5 else 0
        answer = min(cnt[num]+tmp+x, answer)
        return

    # 이렇게만 하면 틀림...
    # tmp = 1 if num%10 > 5 else 0
    # magic(num // 10 + tmp, cnt[num%10] + x)

    if num % 10 <= 5:
        magic(num // 10, cnt[num % 10] + x)
    if num % 10 >= 5:
        magic(num // 10 + 1, cnt[num % 10] + x)


def solution(storey):

    magic(storey, 0)

    print(answer)

    return answer
