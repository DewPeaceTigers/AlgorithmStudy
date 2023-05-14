from itertools import permutations

def solution(k, dungeons):
    answer = -1
    n = len(dungeons)
    nums = [i for i in range(n)]

    for permutation in permutations(nums, n):
        cost = k
        cnt = 0
        for idx in permutation:
            if cost >= dungeons[idx][0]:
                cost -= dungeons[idx][1]
                cnt += 1
        answer = max(answer, cnt)
    return answer