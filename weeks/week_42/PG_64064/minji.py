from itertools import permutations

def check(case, banned_id):
    for i in range(len(banned_id)):
        if len(case[i]) != len(banned_id[i]):
            return False
        for j in range(len(banned_id[i])):
            if (banned_id[i][j] != '*' and banned_id[i][j] != case[i][j]):
                return False
    return True


def solution(user_id, banned_id):
    answer = set()

    for case in list(permutations(user_id, len(banned_id))):  # 제재 아이디 목록
        if check(case, banned_id):
            case = tuple(sorted(case))
            answer.add(case)
    return len(answer)