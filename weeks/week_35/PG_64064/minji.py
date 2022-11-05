'''
1. 가능한 순열 만들기
2. banned_id와 비교하기
'''
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

    for case in list(permutations(user_id, len(banned_id))):
        if check(case, banned_id):
            case = tuple(sorted(case))
            answer.add(case)
    return len(answer)


'''
1. banned_id에 속하는 아이디 찾기
    1-1. user_id가 banned_id에 속하는지 확인
    1-2. 딕셔너리에 추가 key는 banned_id value는 불량 사용자 매핑된 아이디 개수
2. 제재 아이디 목록 몇가지 경우의 수 계산하기
from collections import defaultdict
def solution(user_id, banned_id):
    answer = 1
    banned_id.sort()
    user_id.sort()
    banned_dict=defaultdict(list)

    #key는 banned_id의 인덱스 
    #value는 불량 사용자 매핑된 user_id 인덱스
    for i in range(len(banned_id)):
        for j in range(len(user_id)) :
            if len(banned_id[i])!=len(user_id[j]) :
                continue
            isSame=True
            for k in range(len(banned_id[i])):
                if(banned_id[i][k]!='*' and banned_id[i][k]!=user_id[j][k]) :
                    isSame=False
                    break
            if(isSame) :
                banned_dict[i].append(j)
    print(banned_dict)
    #경우의 수 구현..못하겠음
    return answer
'''