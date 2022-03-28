"""
안입는 옵션을 포함하기
"""
def solution(clothes):
    answer = 1
    types=dict()
    for name, type in clothes:
        if type not in types:
            types[type]=1
        else:
            types[type]+=1
    for type in types: # 타입별로
        answer*=(types[type]+1)
    return answer-1