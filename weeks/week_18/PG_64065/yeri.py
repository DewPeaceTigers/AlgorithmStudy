def solution(strings):
    strings = strings.split('}')
    answer =[]
    for i,string in enumerate(strings):
        strings[i]= string.strip('{').strip(',').strip('{').split(',')
    strings.sort(key=lambda x:len(x))
    for string in strings:
        if string == ['']: continue
        for s in string:
            if s in answer:
                if string.count(s)>answer.count(s): # 여러개라면 넣기
                    answer.append((s))
            else:
                answer.append((s))

    return [ int(a) for a in answer]