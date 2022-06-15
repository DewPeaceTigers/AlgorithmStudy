def solution(n, lost, reserve):
    #lost와 reserve에서 겹치는 학생 제외
    new_lost = set(lost)-set(reserve)
    new_reserve=set(reserve)-set(lost)

    for i in new_reserve :
        if i-1 in new_lost : #체육복을 갖고 있는 학생이 바로 앞 학생에게 빌려주는 경우
            new_lost.remove(i-1)
        elif i+1 in new_lost : #체육복을 갖고 있는 학생이 바로 뒤 학생에게 빌려주는 경우
            new_lost.remove(i+1)
    return n-len(new_lost)