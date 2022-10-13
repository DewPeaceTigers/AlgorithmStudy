import sys
input = sys.stdin.readline

N = int(input())
cranes = list(map(int,input().split()))
M = int(input())
boxes = list(map(int,input().split()))

cranes.sort(key=lambda x:-x)
boxes.sort(key=lambda x:-x)
if cranes[0] < boxes[0]:
    print(-1)
    sys.exit()
time=0
while boxes:
    time+=1
    for crane in cranes:
        for box in boxes:
            if box <= crane:
                boxes.remove(box)
                break
print(time)