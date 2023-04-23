import math
def init(N):
    return [[0]*(N+1),[i for i in range(N+1)],[0]*(N+1)] # result, 부모, rank
def solution(enroll, referral, seller, amount):
    global parent, rank, result 
    index = {}
    for i,e in enumerate(enroll): 
        index[e] = i+1
    result, parent, rank = init(len(enroll))
    def find(n,amount):
        global parent, result
        if amount == 0 : return ## 런타임 에러
        if parent[n]==n:
            result[n]+=amount 
            return
        else:
            mine = math.ceil(amount*0.9)
            result[n]+= mine
            find(parent[n],amount-mine)
            return 
            
    for i,ref in enumerate(referral):
        if ref=="-": 
            parent[i+1] = 0
        else:
            parent[i+1] = index[ref]
        
    
    for i, name in enumerate(seller):
        find(index[name],amount[i]*100)
        
    return result[1:]