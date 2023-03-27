from collections import defaultdict, Counter
def solution(want, number, discount):
    answer = 0
    real = defaultdict(int)
    for i in range(len(want)):
        real[want[i]]=number[i]
    dic = Counter(discount[:10])
    
    for i in range(len(discount)-10+1):
        isOk = True
        for w in want:
            if real[w]!=dic[w]:
                isOk = False
                break
        if isOk:
            answer+=1
        if i+10<len(discount):
            dic[discount[i]]-=1
            dic[discount[i+10]]+=1
            
    return answer