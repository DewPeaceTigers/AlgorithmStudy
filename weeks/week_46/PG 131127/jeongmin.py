def solution(want, number, discount):
    answer = 0
    
    N = len(want)
    
    want_idx = {w:i for i, w in enumerate(want)}    
    
    sales = [0]*N
    for i in range(10):
        if discount[i] in want_idx:
            sales[want_idx[discount[i]]] += 1
    
    possible = 0
    if number == sales:
        possible += 1
    
    for i in range(len(discount)-10): 
        if discount[i] in want_idx:
            sales[want_idx[discount[i]]] -=1
        
        if discount[10+i] in want_idx:
            sales[want_idx[discount[10+i]]] += 1
        
        if number == sales:
            possible += 1
    
    answer = possible
        
    return answer