def solution(s):
    answer = []
    s=s[2:-2]
    s_set=list(s.split('},{'))
    s_set.sort(key=len)
    for s in s_set:
        temp=s.split(',')
        for i in temp :
            if int(i) not in answer:
                answer.append(int(i))
    return answer