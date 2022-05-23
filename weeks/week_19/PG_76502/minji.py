def check(s):
    stack = []
    for c in s:
        if c == '(' or c == '{' or c == '[':
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            x = stack.pop()
            if c == ')' and x != '(':
                return False
            if c == '}' and x != '{':
                return False
            if c == ']' and x != '[':
                return False
    if len(stack) == 0:
        return True


def solution(s):
    answer = 0
    count = 0
    while count != len(s):
        s = s[1:len(s)] + s[0]
        count += 1
        if check(s):
            answer += 1

    return answer