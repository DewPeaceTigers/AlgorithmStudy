from collections import defaultdict
def solution(weights):
answer = 0
weights.sort()
dict_w = defaultdict(int)
for weight in weights:
dict_w[weight]+=1
for w in dict_w:
w4 = w*4
if w4%3==0 and w4//3 in dict_w:
answer+= dict_w[w] * dict_w[w4//3]
if w4%2==0 and w4//2 in dict_w:
answer+= dict_w[w] \* dict_w[w4//2]

        w3 = w*3
        if w3%2==0 and w3//2 in dict_w:
            answer+= dict_w[w] * dict_w[w3//2]

        answer+= dict_w[w]*(dict_w[w]-1)//2

    return answer
