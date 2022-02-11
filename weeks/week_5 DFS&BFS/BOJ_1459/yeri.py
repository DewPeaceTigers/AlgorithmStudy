import sys
input=sys.stdin.readline

x,y,w,s=map(int,input().split())

if 2*w<s:
    print((x+y)*w)
else:
    if w>=s:
        temp = max(x,y)*s
        if (x+y)%2!=0:
            temp+=(w-s)
        print(temp)
    else:
        print(min(x,y)*s+((x-min(x,y)+y-min(x,y))*w))