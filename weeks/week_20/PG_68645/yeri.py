import math
def solution(n):
    res = [[0] * n for _ in range(n)]
    row,col = -1,0
    curNum=1
    for i in range(n):
        for j in range(i,n):
            if i%3==0:
                row+=1
            elif i%3==1:
                col+=1
            else:
                row-=1
                col-=1
            res[row][col]=curNum
            curNum+=1
    arr=[]
    for i in range(n):
        for j in range(n):
            if res[i][j]!=0:
                arr.append(res[i][j])
    return arr