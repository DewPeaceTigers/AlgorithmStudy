def solution(data, col, row_begin, row_end):
    answer = 0
    S = []
    # 2번 과정
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    # print(data)

    # 과정3
    for i in range(row_begin - 1, row_end):
        mod = 0
        for num in data[i]:
            mod += num % (i + 1)
        S.append(mod)

    # 과정 4
    for s in S:
        answer = answer ^ s
    return answer