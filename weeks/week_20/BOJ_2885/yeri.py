import sys
input = sys.stdin.readline

k = int(input())

bin = 1
while bin<k:
    bin*=2
add = 0
time=0
if bin == k :
    print(bin,0)
    sys.exit()
chocolate =bin
while True:
    time+=1
    if add+bin//2 <=k :
        add+=bin//2
    bin //=2
    if add == k: break
print(chocolate,time)