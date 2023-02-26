import re
from collections import defaultdict
def solution(user_id, banned_id):
    global answer,group
    answer = 0 
    reged_id = []
    for id in banned_id:
        temp = ''
        for t in id:
            if t == "*":
                temp+='[a-z0-9]'
            else:temp+=t
        reged_id.append(temp)
    candidate=[]
    for i in range(len(banned_id)):
        id = reged_id[i]
        p = re.compile(id)
        temp = []
        for r_id in user_id: 
            m = p.findall(r_id)
            if m and len(m[0])==len(r_id):
                temp.append(r_id)
        candidate.append(temp)
    def dfs(depth, visit,pair):
        global answer,group
        if depth == len(banned_id):
            pair.sort()
            temp = ''.join(pair)
            if temp not in group:
                group.append(temp)
                answer+=1
            return
        for id in candidate[depth]:
            if visit[id]: continue
            visit[id]=True
            dfs(depth+1,visit,pair+[id])
            visit[id]=False
    visit = dict()
    group = []
    for id in user_id:
        visit[id]=False
    dfs(0,visit,[])
    return answer