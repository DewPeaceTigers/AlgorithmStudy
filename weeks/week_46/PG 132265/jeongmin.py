from collections import Counter

def solution(topping):
    answer = 0
    me = Counter(topping)
    bro = {}
    
    for i in range(len(topping)) :
        if topping[i] in bro :
            bro[topping[i]] += 1
        else :
            bro[topping[i]] = 1
        me[topping[i]] -= 1
        
        if me[topping[i]] == 0 :
            del me[topping[i]]
        
        if len(bro) == len(me) :
            answer +=1
    
    return answer

# 시간 초과..
# def solution(topping):
#     answer = 0
    
#     N = len(topping)
    
#     for i in range(1, N-1):
        
#         me = set(topping[:i])
#         bro = set(topping[i:])
    
#         if len(me) == len(bro):
#             answer += 1
    
#     return answer