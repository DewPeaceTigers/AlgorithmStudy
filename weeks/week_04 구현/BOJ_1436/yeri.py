import sys
input = sys.stdin.readline
n= int(input())
cnt=0
num=0
while cnt!=n :
    num+=1
    if str(num).find('666')!=-1: # 666이 있을 때만 숫자 세기 like 3,6,9 게임처럼
        cnt+=1
print(num)