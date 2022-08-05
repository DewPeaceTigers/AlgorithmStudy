def h(num, start, dest, mid, answer) :
    if num==1:
        return answer.append([start, dest])
    h(num-1, start, mid, dest, answer)
    answer.append([start, dest])
    h(num-1, mid, dest, start, answer)
    
def solution(n):
    answer = []
    h(n, 1, 3, 2, answer)
    return answer