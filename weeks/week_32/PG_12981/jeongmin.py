"""
끝말잇기 규칙
- 1번부터 번호 순서대로 한 사람씩 
- 마지막 사람이 말한 다음에는 다시 1번부터
- 이전에 등장했던 단어 사용 못함
- 단어는 두 글자 이상
"""

def solution(n, words):
    answer = []

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    store = [] # 등장한 단어 저장
    
    num = 0 # 탈락한 사람의 번호 저장
    round = 0 # 자신의 몇 번째 차례에 탈락하는지 저장
    
    for i, word in enumerate(words):                
        # 규칙을 만족하는 경우
        if i==0:
            store.append(word)
            continue
            
        if word not in store and store[-1][-1] == word[0]:
            store.append(word)
            
        else:
            num = i%n + 1 
            round = i//n + 1
            break
        
    answer = [num, round]
    return answer