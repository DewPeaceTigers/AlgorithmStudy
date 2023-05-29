# from collections import defaultdict
# def solution(weights):
#     answer = 0
#     weights.sort()
#     dict_w = defaultdict(int)
#     for weight in weights:
#         dict_w[weight]+=1
#     print(dict_w)
#     for w in dict_w:
#         w4 = w*4 
#         if w4%3==0 and w4//3 in dict_w:
#             answer+= dict_w[w] * dict_w[w4//3]
#         if w4%2==0 and w4//2 in dict_w:
#             answer+= dict_w[w] * dict_w[w4//2]
        
#         w3 = w*3
#         if w3%2==0 and w3//2 in dict_w:
#             answer+= dict_w[w] * dict_w[w3//2]
        
#         answer+= dict_w[w]*(dict_w[w]-1)//2
            
#     return answer

from collections import Counter
def solution(weights):
    answer = 0
    weights.sort()
    w_dict = Counter(weights)
    for w in w_dict:
        w4 = w*4
        if w4%3==0 and w4//3 in w_dict:
            answer+= w_dict[w] * w_dict[w4//3]
        if w4%2==0 and w4//2 in w_dict:
            answer+= w_dict[w] * w_dict[w4//2]
            
        w3 = w*3
        if w3%2==0 and w3//2 in w_dict:
            answer+= w_dict[w] * w_dict[w3//2]
            
        answer += w_dict[w]*(w_dict[w]-1)//2
    return answer
