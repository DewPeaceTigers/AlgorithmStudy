import sys
'''
-기준으로 첫 - 부호가 나오기 전까지는 모두 +
그 이후 모두 -
ex ) 50-55+35
n[0]=50
n[1]=55+35
첫 번째 반복문에서 result = 50
두번째 반복문에서 
result - 55-35 해서 결과
'''
n = input().split('-') #-기준 split
result = 0
for i in n[0].split('+'): #첫 - 부호가 나오기 전
    result += int(i)
for i in n[1:]: #그 이후로는 모두 빼면 됨
    for j in i.split('+'):
        result -= int(j)

print(result)