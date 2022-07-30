
from math import gcd

n=int(input())
trees=[int(input()) for _ in range(n)]
distances=[]

for i in range(1, n) :
    distances.append(abs(trees[i]-trees[i-1])) #������ ���� �Ÿ�

tmp=distances[0]   
for  distance in distances: #�ִ����� ã��
    tmp=gcd(tmp, distance)

answer=(max(trees)-min(trees))//tmp+1 #�ִ������� �������� ���������ϴ� ����
print(answer-len(trees)) #���������ϴ� ����-�̹� ������ ����