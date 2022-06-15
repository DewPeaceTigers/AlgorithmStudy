import sys
H,W=map(int,sys.stdin.readline().split())
world=list(map(int,sys.stdin.readline().split()))
sum=0
for w in range(1,W-1):
    right=max(world[:w])
    left=max(world[w:])

    Min = min(right,left)
    if Min > world[w]:
        sum+=Min-world[w]

    print(w,Min,world[w],Min-world[w])

print(sum)