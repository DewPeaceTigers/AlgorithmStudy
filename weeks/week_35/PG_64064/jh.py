from itertools import permutations


def check(users, banned_id):
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False
        for j in range(len(users[i])):
            if banned_id[i][j] != "*" and banned_id[i][j] != users[i][j]:
                return False
    return True


def solution(user_id, banned_id):
    answer = []
    for com_set in permutations(user_id, len(banned_id)):
        if check(com_set, banned_id):
            com_set = set(com_set)
            if com_set not in answer:
                answer.append(com_set)
    return len(answer)