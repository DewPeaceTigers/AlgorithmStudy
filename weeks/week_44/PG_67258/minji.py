'''
#정확성 통과, 효율성 시간초과
#슬라이싱 때문에

from collections import Counter

def solution(gems):
    answer = []
    gem_kinds = list(set(gems))  # 보석 종류
    n = len(gems)
    start, end = 0, 0
    min_len = float('inf')

    while start < n and end < n:
        tmp = Counter(gems[start:end + 1])
        if len(tmp) == len(gem_kinds):
            answer.append([start + 1, end + 1])
            start += 1
        elif len(tmp) < len(gem_kinds):
            end += 1
        else:
            start += 1
    return sorted(answer, key=lambda x: x[1] - x[0])[0]
'''

#시간초과를 막기 위해 딕셔너리 사용
def solution(gems):
    answer = [0, len(gems)]
    gem_kind = len((set(gems)))  # 보석 종류 개수
    n = len(gems)
    start, end = 0, 0
    gem_dict = {gems[0]: 1}

    while start < n and end < n:
        if len(gem_dict) == gem_kind:
            if end - start < answer[1] - answer[0]:
                answer = [start + 1, end + 1]
            else:
                gem_dict[gems[start]] -= 1
                if gem_dict[gems[start]] == 0:
                    del gem_dict[gems[start]]
                start += 1
        else:
            end += 1
            if end == n: break
            gem_dict[gems[end]] = gem_dict.get(gems[end], 0) + 1
    return answer