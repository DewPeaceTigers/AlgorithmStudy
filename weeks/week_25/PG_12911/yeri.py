def solution(num):
    target = format(num,'b').count('1')
    now=0
    while target!=now :
        num+=1
        now = format(num,'b').count('1')
    return num