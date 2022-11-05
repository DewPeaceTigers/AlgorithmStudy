'''
#효율성 6번만 통과
def solution(gems):
    answer = [0, len(gems)-1]
    gems_kind=set(gems)

    start, end=0, 0
    while start<len(gems) and end<len(gems) :
        if(len(set(gems[start:end+1]))==len(gems_kind)):
                answer=[start, end]
            start+=1
        else:
            end+=1
    answer[0]+=1
    answer[1]+=1
    return answer
'''
def solution(gems):
    answer = [0, len(gems) - 1]
    gems_kind = set(gems)
    dic = {gems[0]: 1}
    start, end = 0, 0
    while start < len(gems) and end < len(gems):
        if len(dic) == len(gems_kind):
            if (end - start) < (answer[1] - answer[0]):
                answer = [start, end]
            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            start += 1
        else:
            end += 1
            if end == len(gems):
                break
            dic[gems[end]] = dic.get(gems[end], 0) + 1

    answer[0] += 1
    answer[1] += 1
    return answer