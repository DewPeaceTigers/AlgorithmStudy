import sys
input = sys.stdin.readline

N, K = map(int,input().split())
num = list(map(int,list(input().strip())))
res = []

for i in range(N):
    while K>0 and res:
        if res[-1] < num[i]:
            res.pop()
            K-=1
        else: break # 크거나 같으면 넣어주기
    res.append(num[i])

print(''.join(list(map(str,res[:N-K]))))