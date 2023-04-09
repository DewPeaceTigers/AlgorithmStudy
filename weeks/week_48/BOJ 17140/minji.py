import sys
from collections import Counter

input=sys.stdin.readline

def calc_r(matrixs): #r연산
    new=[]
    max_length=0
    for i in range(len(matrixs)) :
        new_row=[]
        tmp=Counter(matrixs[i])
        del tmp[0] #0제외

        tmp=list(tmp.items())
        tmp.sort(key=lambda x:(x[1], x[0])) #오름차순 정렬

        #길이가 100이 넘어가면 자르기
        if len(tmp)>50 :
            tmp=tmp[50:]

        for t in tmp :
            new_row.append(t[0])
            new_row.append(t[1])
        new.append(new_row)
        max_length=max(max_length, len(new_row))

    #가장 긴 리스트에 맞춰 0 채우기
    for i in range(len(new)) :
        while len(new[i])!=max_length :
            new[i].append(0)

    return new


r, c, k=map(int, input().split())
matrixs=[list(map(int, input().split())) for i in range(3)]

for i in range(101) :
    try:
        if matrixs[r-1][c-1]==k :
            print(i)
            break
    except:
        pass

    if len(matrixs)>=len(matrixs[0]) :
        matrixs=calc_r(matrixs)
    else:
        matrixs=list(map(list, zip(*matrixs)))
        matrixs=calc_r(matrixs)
        matrixs=list(map(list, zip(*matrixs)))
else:
    print(-1)

