def solution(clothes):
    answer = {}
    for cloth in clothes:
        if cloth[1] in answer:
            answer[cloth[1]] += 1
        else:
            answer[cloth[1]] = 1

    count = 1
    for i in answer.values():
        count *= (i + 1)

    return count - 1