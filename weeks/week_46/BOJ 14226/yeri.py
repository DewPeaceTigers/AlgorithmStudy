import sys
from collections import deque
input = sys.stdin.readline

S = int(input())

q = deque([[1,0,0]])
answer=0
visit = set()
while q:
    emoticon, time, clipboard = q.popleft()

    if emoticon == S:
        answer = time
        break
    if emoticon > S:
        continue

    if str(emoticon)+" "+str(time+1)+" "+str(emoticon) not in visit:
        q.append([emoticon,time+1,emoticon])
        visit.add(str(emoticon)+" "+str(time+1)+" "+str(emoticon))
    if str(emoticon+clipboard)+" "+str(time+1)+" "+str(clipboard) not in visit and clipboard!=0:
        q.append([emoticon+clipboard, time+1, clipboard])
        visit.add(str(emoticon+clipboard)+" "+str(time+1)+" "+str(clipboard))
    if str(emoticon-1)+" "+str(time+1)+" "+str(clipboard) not in visit and emoticon-1!=0:
        q.append([emoticon-1,time+1,clipboard])
        visit.add(str(emoticon-1)+" "+str(time+1)+" "+str(clipboard))
print(answer)