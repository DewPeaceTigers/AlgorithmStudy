def solution(s):
    time=0
    zero=0
    while s!='1':
        time+=1
        newS = s.replace('0','')
        zero += len(s)-len(newS)
        s = format(len(newS),'b')
    return [time,zero]