def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees :
        s=""
        for sk in skill_tree :
            if sk in skill:
                s+=sk
        if skill[:len(s)]==s :
            answer+=1
    return answer