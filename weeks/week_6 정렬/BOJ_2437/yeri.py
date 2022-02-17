import sys

N = int(input())

weightList = list(map(int,sys.stdin.readline().split()))
weightList.sort()

result = 0
for i in range(N):
    if result + 1 >= weightList[i]:
        result += weightList[i]
    else:
        break

print(result + 1)