import sys
from collections import deque
n = int(input())
q = deque([])
for i in range(n) :
    command = sys.stdin.readline()
    if command.startswith("push") :
        item = command.split()
        q.append(item[1])
    elif command.startswith("pop") :
        if len(q) == 0 :
            print("-1")
        else :
            print(q.popleft())
    elif command.startswith("size") :
        print(len(q))
    elif command.startswith("empty") :
        if len(q) == 0 :
            print(1)
        else :
            print(0)
    elif command.startswith("front") :
        if len(q) == 0 :
            print(-1)
        else :
            print(q[0])
    elif command.startswith("back") :
        if len(q) == 0 :
            print(-1)
        else :
            print(q[-1])