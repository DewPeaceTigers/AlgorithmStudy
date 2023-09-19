from itertools import permutations
from collections import deque
def solution(expression):
    answer = 0
    nums = []
    ops = []
    expression = deque(expression)
    num = ''
    while expression:
        f = expression.popleft()
        
        if f.isnumeric():
            num+=f
        else:
            nums.append(num)
            num=''
            ops.append(f)
    nums.append(num)
    
    for perms in permutations(['+','-','*'],3):
        newNums = list(map(int,nums))
        newOps = ops[:]
        for op in perms:
            nomore = False
            while not nomore:
                nomore = True
                for i in range(len(newOps)):
                    if newOps[i] == op:
                        nomore = False
                        res = 0
                        if op=='+':
                            res = newNums[i]+newNums[i+1]
                        elif op=='-':
                            res = newNums[i]-newNums[i+1]
                        else:
                            res = newNums[i]*newNums[i+1]
                        newNums = newNums[:i]+[res]+newNums[i+2:]
                        newOps = newOps[:i]+newOps[i+1:]
                        break
        answer = max(abs(newNums[0]),answer)
    return answer
