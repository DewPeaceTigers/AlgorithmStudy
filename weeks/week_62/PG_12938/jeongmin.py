def solution(n, s):
    answer = []

    if s < n:
        return [-1]

    # s을 n으로 나눴을 때 몫, 나머지
    x, remain = divmod(s, n)
    # print(x, remain)

    # (n-remain)개는 x, 나머지 remain개는 (x+1)
    answer = [x]*(n-remain) + [x+1]*remain

    return answer
