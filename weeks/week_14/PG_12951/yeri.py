def solution(s):
    answer = ''
    temps = s.split(' ')
    for j,temp in enumerate(temps):
        for i,t in enumerate(list(temp)):
            if i==0 and t.isalpha(): t=t.upper()
            else : t=t.lower()
            answer+=t
        if j!=len(temps)-1: answer+=' '
    return answer