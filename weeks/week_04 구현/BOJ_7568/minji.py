'''
n이 최대 50이니까 아무리 많이 비교해도 2500번
한명씩 돌아가면서 n명과 비교

자기보다 덩치 큰 사람이 있을 때마다 count 1증가
count 값이 등수
'''
import sys
n=int(sys.stdin.readline())
data = []
for i in range(n) :
    a, b=map(int, sys.stdin.readline().split())
    data.append((a, b))

for i in range(n) :
    count=1
    for j in range(n) :
        if data[i][0] < data[j][0] and data[i][1] < data[j][1] : #자기보다 덩치 큰 사람 마다 count 1증가
            count+=1
    print(count, end=' ')

