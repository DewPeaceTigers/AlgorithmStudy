from itertools import combinations
def solution(relation):
    answer = []
    col_n = len(relation[0])
    cols = [ i for i in range(col_n)]
    for i in range(1,col_n+1):
        for c in combinations(cols,i):
            check = set()
            for r in range(len(relation)):
                keys = ()
                for c_idx in c:
                    keys+=(relation[r][c_idx],)
                if len(keys) == len(c):
                    keys=tuple(sorted(list(keys)))
                    if keys in check: break
                    check.add(keys)
            if len(check) == len(relation):
                answer.append(c)
    res = 0
    done = [True]*len(answer)
    for a,ans in enumerate(answer):
        if not done[a]: continue
        for j in range(a+1,len(answer)):
            isDone = 0
            for i in range(len(ans)):
                if ans[i] in answer[j]:
                    isDone+=1
            if isDone == len(ans):
                done[j] = False
    return done.count(True)