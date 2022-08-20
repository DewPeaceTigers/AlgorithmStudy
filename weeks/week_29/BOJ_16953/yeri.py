import sys
input = sys.stdin.readline

a,b = map(int,input().split())
cnt=0
while a<b:
    cnt+=1
    b = str(b)
    if b[-1]=='1':
        b = int(b[:-1])
    else :
        b = int(b)
        if b%2!=0: break
        b = b//2
print(cnt+1 if a==b else -1)