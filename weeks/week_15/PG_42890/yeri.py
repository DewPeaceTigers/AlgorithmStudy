from itertools import combinations
def solution(relations):
    answer = 0
    cand_keys=[]
    types=[i for i in range(len(relations[0]))]
    for i in range(1,len(relations)):
        for keys in combinations(types,i):
            arr=[]
            for relation in relations:
                arr.append(tuple([relation[key] for key in keys]))
            temp = set(arr)
            if len(temp)==len(arr):
                # 유일함
                isMin=True
                set_keys=set(keys)
                for cand_key in cand_keys:
                    if len(set(cand_key) & set_keys)==len(cand_key):
                        isMin=False
                        break
                if isMin: cand_keys.append(keys)
    return len(cand_keys)