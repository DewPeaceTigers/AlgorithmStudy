def solution(picks, minerals):
    global answer
    answer = int(1e9)
    piro = [
        { "diamond":1, "iron":1, "stone":1},
        {"diamond":5,"iron":1,"stone":1},
        {"diamond":25,"iron":5,"stone":1}
    ]
    
    def dfs(depth,total,pick,route):
        global answer
        if total > answer: return
        if depth == len(minerals) or sum(pick) == 0:
            answer = min(answer,total)
            return
        for i in range(len(pick)):
            if pick[i] == 0: continue
            current = 0
            until = min(depth+5,len(minerals))
            for t in range(depth,until):
                current += piro[i][minerals[t]]
            dfs(until,total+current,pick[:i]+[pick[i]-1]+pick[i+1:],route+str(i)+"->")
    dfs(0,0,picks[:],"")
    return answer