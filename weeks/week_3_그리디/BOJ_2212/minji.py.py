'''
n : 센서 개수
k : 집중국 개수
sensor[] : 센서 좌표
'''
import sys

n=int(input())
k=int(input())
sensor = list(map(int, sys.stdin.readline().split()))
sensor.sort()
dist = []
for i in range(n-1) : #센서 거리 차
    dist.append(sensor[i+1]-sensor[i])

dist.sort()
if k > n : #집중국 수가 크면 센서 위치에 설치하므로 0
    print(0)
else :
    for i in range(k-1) : #오름차순 정렬 후 집중국 수-1 만큼 제외
        dist.pop()
    min = sum(dist)
    print(min)
