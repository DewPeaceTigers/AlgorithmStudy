from collections import deque
def solution(people, limit):
    people.sort(key=lambda x:-x)
    l = 0
    r = len(people)-1
    cnt = 0
    while l<r:
        sum = people[l]+people[r]
        if sum <= limit:
            l+=1
            r-=1
        else:
            l+=1
        cnt+=1
    if l==r:
        cnt+=1
    return cnt
            