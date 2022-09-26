'''
중간값으로 구한 결과가 곱했을 때 최대가 나옴
'''
def solution(n, s):
    answer = []
    if n>s :
        return [-1]
    init=s//n
    for _ in range(n) :
        answer.append(init)
    pos=len(answer)-1
    '''
    합을 계속하면 효율성문제
    while sum(answer)<s : 
        answer[pos]+=1
        pos-=1
    '''
    for i in range(s%n) :
        answer[pos]+=1
        pos-=1
    return answer