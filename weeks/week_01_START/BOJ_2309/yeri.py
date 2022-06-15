from itertools import combinations as cb
dwarf=[]
for _ in range(9):
    dwarf.append(int(input()))
dwarf.sort(reverse=True)
sum_of_excess_dwarf=abs(100-sum(dwarf))
excess=()
for pair in cb([i for i in range(9)],2):
    if dwarf[pair[0]]+dwarf[pair[1]]==sum_of_excess_dwarf: break

for i in range(8,-1,-1):
    if i==pair[0] or i==pair[1]: continue
    print(dwarf[i])