from collections import deque
def solution(cards):
    global opened
    answer = 0
    for i in range(len(cards)):
        cards[i] -=1
    
    def find(n,pivot,cnt):
        global opened
        if opened[n]: return 0
        opened[n] = True
        if cards[n] == pivot : return cnt+1
        return find(cards[n],pivot,cnt+1)
    
    opended=[]
    best = 0
    for i in range(len(cards)):
        opened = [False]*len(cards)
        first = find(i,i,0)
        sec = 0
        temp = opened[:]
        for j in range(len(cards)):
            if i==j: continue
            opened = temp
            sec = max(find(j,j,0),sec)
        best = max(best, first*sec)
    return best