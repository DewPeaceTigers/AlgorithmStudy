from collections import defaultdict
def findOne(piv, words):
    temp=[]
    for word in words:
        if word == piv : continue
        cnt = 0
        for i in range(len(piv)):
            if piv[i]!=word[i]:
                cnt+=1
            if cnt >1 : break
        if cnt == 1: temp.append(word)
    return temp
    for i,word in enumerate(words):
        word = set(word)
        print(piv&word)
        if len(piv & word) == 2:
            temp.append(words[i])
    return temp
def solution(begin, target, words):
    if target not in words: return 0
    dic = defaultdict(list)
    dic[begin] = findOne(begin,words)
    for word in words:
        dic[word] = findOne(word,words)
    
    stack = [[begin,0]]
    minCnt = int(1e9)
    visited = {begin}
    while stack:
        now, cnt = stack.pop()
        if cnt > minCnt : continue
        if now == target:
            minCnt = min(cnt,minCnt)
            continue
        for change in dic[now]:
            if change in visited: continue
            stack.append([change,cnt+1])
            visited.add(change)
    return minCnt if minCnt!=int(1e9) else 0