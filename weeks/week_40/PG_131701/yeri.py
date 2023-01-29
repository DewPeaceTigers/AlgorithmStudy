def solution(elements):
    answer = set()
    for long in range(1,len(elements)+1):
        temp = sum(elements[:long])
        for i in range(len(elements)):
            answer.add(temp)
            temp -= elements[i]
            if i+long<len(elements): temp += elements[i+long]
            else: temp += elements[i+long-len(elements)]
    return len(answer)