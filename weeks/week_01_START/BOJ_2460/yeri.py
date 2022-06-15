count_ppl=[0,]
for i in range(10):
    off,on=map(int,input().split())
    count_ppl.append(count_ppl[-1]+on-off)
print(max(count_ppl))