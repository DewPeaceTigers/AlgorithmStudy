def solution(word):
    answer = 0
    dict_ = {
        'A':0,
        'E':1,
        'I':2,
        'O':3,
        'U':4
    }
    gap = [3905//5,3905//25,3905//125,3905//625,3905//3125]
    print(gap)
    for i,w in enumerate(word):
        if w=='A':
            answer+=1
        else :
            answer+=dict_[w]*gap[i]+1
    return answer