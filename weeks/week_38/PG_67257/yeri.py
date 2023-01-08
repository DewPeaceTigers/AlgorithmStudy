def solution(expression):
    global ops, operands, operators, max_n
    temp = ''
    operands, operators = [], []
    for ex in expression:
        if ex.isnumeric():
            temp += ex
        else:
            operands.append(int(temp))
            operators.append(ex)
            temp = ""
    operands.append(int(temp))
    def calc(cand):
        global operands, operators
        rands = operands[:]
        rators = operators[:]
        for c in cand:
            while c in rators:
                i = rators.index(c)
                if c == rators[i]:
                    if c == '+':
                        rands[i] = rands[i] + rands[i+1]
                    elif c == "-":
                        rands[i] = rands[i] - rands[i+1]
                    else:
                        rands[i] = rands[i] * rands[i+1]

                    del rands[i+1]
                    del rators[i]
        return abs(rands[0])
    def perm(depth, cand, checked):
        global ops, max_n
        if depth == 3:
            max_n = max(calc(cand),max_n)
            return
        for i in range(3):
            if checked[i]: continue
            checked[i] = True
            perm(depth + 1, cand + [ops[i]], checked)
            checked[i] = False

    ops = ['+', '*', '-']
    max_n = 0
    perm(0, [], [False, False, False])
    return max_n