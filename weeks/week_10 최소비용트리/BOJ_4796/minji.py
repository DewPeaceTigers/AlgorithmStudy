import sys
input=sys.stdin.readline

i=1
while True:
    l, p, v=map(int, input().split())
    if l+p+v == 0:
        break
    ans=(v//p)*l
    ans+=min(v%p, l)
    print("Case %d: %d" %(i, ans))
    i+=1