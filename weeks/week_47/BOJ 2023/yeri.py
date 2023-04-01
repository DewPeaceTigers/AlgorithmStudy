import sys
input = sys.stdin.readline

N = int(input())

one = [2,3,5,7]
answer = []
def make(depth, now):
    now = int(now)
    if depth!=1:
        for i in range(2,int(now**0.5+1)):
            if now%i==0: return
        if depth==N:
            answer.append(now)
            return
    for i in range(1,10,2):
        make(depth+1,str(now)+str(i))
if N==1:
    for a in one: print(a)
    sys.exit()

for i in one:
    make(1,str(i))

for a in answer: print(a)