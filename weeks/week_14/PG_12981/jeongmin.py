"""
풀이 방법
- 사람의 번호 : i%n + 1 (나머지 이용)
- 라운드 : i//n + 1 (몫 이용)
"""

def solution(n, words):
    store = [] # 등장한 단어 저장
    
    num = 0 # 탈락한 사람의 번호 저장
    round = 0 # 자신의 몇 번째 차례에 탈락하는지 저장
    
    for i, word in enumerate(words):        
        # # 단어가 한 글자 (문제 제한 사항 - 단어의 길이는 2 이상 50 이하)
        # if len(word) == 1:
        #     break
        
        # 등장했던 단어인 경우
        if word in store:
            num = i%n + 1 
            round = i//n + 1
            break
        
        # 이전 마지막 문자, 현재 앞문자 확인
        if store and store[-1][-1] != word[0]:
            num = i%n + 1 
            round = i//n + 1
            break
        
        store.append(word)
        
    answer = [num, round]
    return answer


"""
[다른 사람 풀이] 
코드가 정말 짧다.
등장했던 단어를 저장하는 리스트를 만들 필요 없이 words[:p]를 사용해 확인!
"""
# def solution(n, words):
#    for p in range(1, len(words)):
#        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
#    else:
#        return [0,0]