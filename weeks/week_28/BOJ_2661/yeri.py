import sys
input = sys.stdin.readline

N = int(input())
visited = [0]*3

min_arr=0
def find(cnt, temp):
    global min_arr
    if min_arr!=0 : return
    for i in range(1,(cnt//2)+1):
        if temp[-i:] == temp[-2*i:-i] : return
    if cnt == N:
        min_arr = ''.join(temp)
        return
    for i in range(1,4):
        temp.append(str(i))
        find(cnt+1,temp)
        temp.pop()
find(0,[])
print(min_arr)
