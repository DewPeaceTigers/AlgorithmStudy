def solution(n, s):
    # answer = []
    # while s != 0:
    #     answer.append(s//n)
    #     if answer[-1]==0: return [-1]
    #     s -= answer[-1]
    #     n -=1
    # return answer
    answer = []
    a = int(s/n)

    if a == 0:
        return [-1]

    b = s%n

    for i in range(n-b):
        answer.append(a)
    for i in range(b):
        answer.append(a+1)

    return answer