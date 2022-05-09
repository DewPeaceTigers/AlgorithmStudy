import itertools
def solution(expression):
    temp=''
    operands,operators=[],[]
    for e in expression:
        if e.isnumeric() :
            temp+=e
        else:
            operands.append(int(temp))
            temp=''
            operators.append(e)
    operands.append(int(temp))
    sums=[]
    for rators  in itertools.permutations(['+', '-', '*']):
        t_rators=operators[:]
        t_rands=operands[:]
        for r in rators:
            while r in t_rators:
                o = t_rators.index(r)
                if t_rators[o] == '+':
                    sum = (t_rands[o]+t_rands[o+1])
                elif t_rators[o] == '-':
                    sum = (t_rands[o] - t_rands[o + 1])
                elif t_rators[o] == '*':
                    sum = (t_rands[o]*t_rands[o+1])
                t_rands[o]=sum
                del t_rands[o+1]
                del t_rators[o]
        sums.append(abs(t_rands[0]))
    return max(sums)