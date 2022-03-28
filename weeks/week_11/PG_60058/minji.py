def check(u):
    stack = []
    for i in u:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True


def divide(p):
    open = 0
    close = 0
    for i in range(len(p)):
        if p[i] == '(':
            open += 1
        else:
            close += 1
        if open == close:
            return p[:i + 1], p[i + 1:]


def solution(p):
    answer = ''
    if p == "":  # 과정1 빈 문자열
        return answer

    # 과정 2 u, v로 분리
    u, v = divide(p)

    # 과정 3
    if check(u):  # u가 올바른 문자열인 경우 나머지 v는 과정1부터 다시
        return u + solution(v)
    else:
        # 과정 4-1
        answer += '('
        # 과정 4-2
        answer += solution(v)
        # 과정 4-3
        answer += ')'
        # 과정 4-4
        for i in range(1, len(u) - 1):
            if u[i] == ')':
                answer += '('
            else:
                answer += ')'
        # 과정 4-5
        return answer
