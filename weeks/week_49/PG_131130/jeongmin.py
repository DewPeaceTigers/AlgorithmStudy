# 게임의 점수 = (1번 상자 그룹에 속한 상자의 수) * (2번 상자 그룹에 속한 상자의 수)

from itertools import permutations

def solution(cards):
    answer = 0
    
    N = len(cards)
    box_num = range(N)
    
    # 임의로 두 개의 숫자 선택 (첫번째 상자그룹, 두번째 상자그룹 시작 번호)
    cases = permutations(box_num, 2)
    
    # 모든 경우 확인
    for case in cases:
        first, second = case
        
        # 각 상자 그룹에 속한 상자의 수 
        first_cnt, second_cnt = 0, 0
        
        # 열려있는지 확인
        check = [False] * N
        
        # 첫번째 상자 그룹 
        while not check[first]:
            check[first] = True
            first_cnt += 1
            first = cards[first]-1
        # print("첫번째", check)
        
        # 두번째 상자그룹 시작 번호에 해당하는 상자가 이미 열려있는 경우 넘어감
        if check[second]:
            continue
            
        while not check[second]:
            check[second] = True
            second_cnt += 1
            second = cards[second]-1
        # print("두번째", check)
        
        answer = max(answer, first_cnt * second_cnt)
    return answer