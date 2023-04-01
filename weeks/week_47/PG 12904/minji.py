def check(tmp) :
    if tmp==tmp[::-1] :
        return True
    return False

def solution(s):
    answer = 0

    for i in range(len(s)) :
        for j in range(i+1, len(s)+1) :
            if check(s[i:j]) :
                if answer<len(s[i:j]) :
                    answer=len(s[i:j])
    return answer