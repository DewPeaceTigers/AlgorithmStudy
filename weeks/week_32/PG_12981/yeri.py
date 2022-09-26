import math
def solution(n,words):
    set_words = set()
    answer=[0,0]
    bef = ""
    for i, word in enumerate(words):
        if i==0:
            bef = word
            set_words.add(word)
            continue
        if bef[-1]!=word[0]:
            answer = [i%n+1,math.ceil((i+1)/n)]
            break
        bef = word
        if word in set_words:
            first = words.index(word)
            sec = words.index(word,first+1)
            answer = [sec%n+1,math.ceil((sec+1)/n)]
            break
        else:
            set_words.add(word)
    return answer