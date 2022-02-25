# 못품
# 이해 못함
def count(li, m):
    t = 0
    for n in li:
        if n >= m:
            break
        t += m-n
    return t

N, K = map(int, input().split())
li = sorted([int(input()) for _ in range(N)])
s, e = min(li), max(li)+K
res = 0
while s <= e:
    m = (s+e)//2
    if count(li, m) <= K:
        res = m
        s = m+1
    else:
        e = m-1
print(res)
