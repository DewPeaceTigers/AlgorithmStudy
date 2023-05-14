from itertools import permutations
def solution(k, dungeons):
    answer = 0
    for c in list(permutations([i for i in range(len(dungeons))],len(dungeons))):
        now = k
        cnt = 0
        for n in c:
            need, use = dungeons[n]
            if now < need: break
            cnt+=1
            now -= use
        answer = max(cnt,answer)
    return answer