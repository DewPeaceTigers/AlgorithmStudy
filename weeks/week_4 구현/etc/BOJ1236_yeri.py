# 모든 행과 열에 한 명 이상의 경비원이 있어야 함
# 행 기준, 열 기준으로 필요한 경비원의 수를 각각 계산하여 더 큰 수 출력
# 행 기준으로 몇 개의 행이 경비원이 없는지
# 열 기준으로 몇 개의 열이 경비원이 없는지

n,m = map(int,input().split())
array=[]

for _ in range(n):
    array.append(input())

row=[0]*n
column=[0]*m

for i in range(n):
    for j in range(m):
        if array[i][j]=='X':
            row[i]=1
            column[j]=1
# 없는 부분을 세기 
row_count=0
for i in range(n):
    if row[i]==0: 
        row_count+=1
column_count=0
for j in range(m):
    if column[j]==0:
        column_count+=1
print(max(row_count,column_count))