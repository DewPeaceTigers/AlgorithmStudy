'''
최소성을 어떻게 체크해야할지 모르겠어서 풀이 참고
'''
from itertools import combinations


def solution(relation):
    answer = []
    candidate_key = []
    col = len(relation[0])
    row = len(relation)
    # 유일성
    for i in range(1, col + 1):
        for comb in combinations(range(col), i):
            tmp = [tuple(record[c] for c in comb) for record in relation]
            if len(set(tmp)) == row:  # 최소성
                put = True
                for x in candidate_key:
                    if set(x).issubset(set(comb)):
                        put = False
                        break
                if put:
                    candidate_key.append(comb)

    return len(candidate_key)