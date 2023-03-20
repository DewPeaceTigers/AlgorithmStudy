from collections import deque
def solution(p):
    def isLeft(e):
        if e == '(':
            return True
        else:
            return False

    def isFine(u):
        stack = [u[0]]
        for idx in range(1, len(u)):
            if isLeft(u[idx]):
                stack.append(u[idx])
            else:
                if not stack:
                    stack.append(u[idx])
                    continue
                if isLeft(stack[-1]):
                    stack.pop()
                else: return False
            idx += 1
        if stack:
            return False
        else:
            return True
    def reversing(u):
        temp=''
        for t in u[1:len(u)-1]:
            if isLeft(t): temp+=')'
            else: temp+='('
        return temp
    def make(w):
        if not w or isFine(w): return ''.join(w)
        answer = ''
        u = []
        v = w
        while v:
            l = 0
            r = 0
            while True:
                f = v.popleft()
                if isLeft(f):
                    l += 1
                else:
                    r += 1
                u.append(f)
                if l==r: break
            if isFine(u):
                answer += ''.join(u)
                u = []
            else:
                temp = '(' + make(v) + ')' + reversing(u)
                return answer+temp
        return answer

    return make(deque(p))