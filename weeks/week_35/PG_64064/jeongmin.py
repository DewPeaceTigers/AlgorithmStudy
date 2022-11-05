import re
from itertools import permutations 

def solution(user_id, banned_id):
    n = len(banned_id)
    banned_id = [i.replace("*", ".") for i in banned_id]
    answer = []

    for i in permutations(user_id, n):
        lst = list(i)
        flag = True
        for j in range(n):
            if re.match(banned_id[j], lst[j]) and (len(banned_id[j]) == len(lst[j])) :
                continue 
            else:
                flag = False
                break
        if flag:
            if sorted(lst) not in answer:
                answer.append(sorted(lst))

    return len(answer) 
