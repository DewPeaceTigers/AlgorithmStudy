def solution(n, words):
    answer = [0, 0]

    for i in range(1, len(words)):
        if words[i] in words[:i]:
            answer = [i % n + 1, i // n + 1]
            break
        if words[i][0] != words[i - 1][-1]:
            answer = [i % n + 1, i // n + 1]
            break

    return answer