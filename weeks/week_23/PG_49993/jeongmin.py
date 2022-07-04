# 가능한 스킬트리 개수
def solution(skill, skill_trees):
    answer = 0
    
    not_skill = [chr(ord('A')+i) for i in range(26)]
    skill = list(skill)
    for sk in skill:
        not_skill.remove(sk)
    
    for skill_tree in skill_trees:
        for s in not_skill:
            skill_tree = skill_tree.replace(s, "")
            
        answer += 1
        for i in range(len(skill_tree)):
            if skill_tree[i] != skill[i]:
                answer -= 1
                break
                
    return answer

""" 다른사람 코드 .."""
# def solution(skill,skill_tree):
#     answer=0
#     for i in skill_tree:
#         skillist=''
#         for z in i:
#             if z in skill:
#                 skillist+=z
#         if skillist==skill[0:len(skillist)]:
#             answer+=1
#     return answer

