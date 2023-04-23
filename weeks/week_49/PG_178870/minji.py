'''
33번 테케 때문에 고생함...
sequence = [5, 5, 5, 5, 5, 5], k=5인경우

'''
def solution(sequence, k):
    n = len(sequence)
    answer = [0, n - 1]

    start, end = 0, 0
    total = sequence[0]

    while start < n and end < n:
        if total == k:
            if answer[1] - answer[0] > end - start:
                answer = [start, end]
            total -= sequence[start]
            start += 1
        elif total > k:
            total -= sequence[start]
            start += 1
        else:
            end += 1
            if end == n:
                break
            total += sequence[end]

    return answer