import math
def solution(n, words):
    answer = [0,0]
    for i,word in enumerate(words):
        if i==0: continue
        if words[i-1][-1]!=word[0] or word in words[:i]:
            # 끝말잇기가 아니라면 탈락 # 앞에서 나온 것과 중복이라면
            answer=[i%n+1,math.ceil((i+1)/n)]
            break
    return answer