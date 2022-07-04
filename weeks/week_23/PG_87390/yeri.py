def solution(n, left, right):
    answer = []
    for num in range(left,right+1):
        r = num//n
        c = num %n

        if c <= r:
            answer.append(r+1)
        elif c>r:
            answer.append(c+1)
    return answer
