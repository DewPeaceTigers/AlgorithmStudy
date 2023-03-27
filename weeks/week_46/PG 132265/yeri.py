from collections import defaultdict,Counter
def solution(topping):
    answer = 0
    left = Counter(topping[:1])
    right = Counter(topping[1:])
    l = len(left)
    r = len(right)
    
    for i in range(len(topping)-1):
        if l==r: answer+=1
        
        now = topping[i+1]
        left[now]+=1
        right[now]-=1
        if right[now]==0:
            r-=1
        l = len(left)
        
    return answer