from collections import defaultdict
def solution(k, tangerine):
    answer = 0
    dict_t = defaultdict(int)
    for t in tangerine:
        dict_t[t]+=1
    list_t = list(dict_t.items())
    list_t.sort(key=lambda x:x[1])
    while k>0:
        key, val = list_t.pop()
        answer+=1
        k-=val
    return answer