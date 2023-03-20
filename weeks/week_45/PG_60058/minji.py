def divide(p):
    left, right = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return p[:i + 1], p[i + 1:]


def check(p):
    stack = []

    for ch in p:
        if ch == '(':
            stack.append(ch)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    return False


def solution(p):
    answer = ''

    # 과정 1
    if len(p) == 0: return p

    # 과정 2
    u, v = divide(p)

    # 과정 3
    if check(u):
        return u + solution(v)
    else:  # 과정 4
        answer = '('
        answer += solution(v)
        answer += ')'
        for ch in u[1:len(u) - 1]:
            if ch == '(':
                answer += ')'
            else:
                answer += '('
    return answer