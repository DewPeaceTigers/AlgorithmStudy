import sys
from collections import Counter
input = sys.stdin.readline

r,c,k = map(int,input().split())
arrs = []

for _ in range(3):
    arrs.append(list(map(int,input().split())))

def change(temp):
    temp = list(Counter(temp).items())
    temp.sort(key=lambda x: (x[1], x[0]))
    n_temp = []
    for n, cnt in temp:
        if n == 0: continue
        n_temp.append(n)
        n_temp.append(cnt)
    return n_temp

answer = 0
while answer<=100:
    if r-1 <len(arrs) and c-1<len(arrs[0]) and arrs[r-1][c-1]==k: break
    answer+=1
    if len(arrs)>=len(arrs[0]):
        # R 연산
        for i,arr in enumerate(arrs):
            arrs[i]= change(arr)
        max_r = 0
        for arr in arrs: max_r = max(max_r,len(arr))
        max_r = min(max_r,100)
        max_r = max(max_r,3)
        for i in range(len(arrs)):
            arrs[i]+=[0]*(max_r-len(arrs[i]))
    else:
        # C 연산
        new_temps = []
        for j in range(len(arrs[0])):
            temp = []
            for i in range(len(arrs)):
                temp.append(arrs[i][j])
            temp = change(temp)
            new_temps.append(temp)
        max_c = 0
        for temp in new_temps: max_c = max(max_c,len(temp))
        max_c = min(max_c,100)
        max_c = max(max_c,3)
        arrs = [[0]*len(new_temps) for _ in range(max_c)]
        for j in range(len(new_temps)):
            for i in range(len(new_temps[j])):
                arrs[i][j] = new_temps[j][i]
if r-1 <len(arrs) and c-1<len(arrs[0]) and arrs[r-1][c-1]==k: print(answer)
else: print(-1)