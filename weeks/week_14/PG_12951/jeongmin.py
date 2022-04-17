# JadenCase 문자열
# - 모든 단어의 첫 문자 : 대문자, 그 외의 알파벳 : 소문자
# - 단, 첫 문자가 알파벳이 아닐 때에는 알파벳은 소문자로 쓰면 됨

# 주어진 조건 잘 확인하기!
# 공백문자가 연속해서 나올 수 있습니다...

def solution(s):
    answer = ''
    
    # 문자열 s에 있는 단어 리스트로 저장
    words = s.split(' ')
    
    for i, word in enumerate(words):
        if word == '': # 공백문자일 경우
            continue
            
        # JadenCase로 바꾼 단어
        w = ''
        
        # 첫 문자가 알파벳일 경우 대문자로
        if word[0].isalpha():
            w = word[0].upper()
            
        # 첫 문자가 숫자인 경우
        else:
            w = word[0]
            
        # 그 외의 알파벳은 소문자
        w += word[1:].lower()
        
        # 변환한 단어 저장
        words[i] = w
        
    answer = " ".join(words)
    
    return answer

"""
[다른 사람 풀이 (완전 간단한 코드!)]
capitalize() 함수 사용
- 문자열의 첫 글자는 대문자로, 나머지는 소문자로 변환한다.
"""
# def solution(s):
#     return ' '.join([word.capitalize() for word in s.split(" ")])