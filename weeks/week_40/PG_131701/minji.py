def solution(elements):
    answer = set()
    length = len(elements)
    elements = elements * 2

    for i in range(length):
        for j in range(length):
            answer.add(sum(elements[j:j + i + 1]))
    return len(answer)