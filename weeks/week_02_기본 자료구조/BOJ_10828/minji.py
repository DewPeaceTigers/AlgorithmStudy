import sys

n = int(input())
temp = []
for i in range(n) :
    k = sys.stdin.readline()
    if k.startswith('pop') :
        if len(temp) == 0:
            print(-1)
        else:
            print(temp.pop())
    elif k.startswith('size') :
        print(len(temp))
    elif k.startswith('top') :
        if len(temp) == 0 :
            print(-1)
        else :
            print(temp[-1])
    elif k.startswith('empty') :
        if len(temp) == 0 :
            print(1)
        else :
            print(0)
    elif k.startswith('push') :
        s = k.split()
        temp.append(s[1])
