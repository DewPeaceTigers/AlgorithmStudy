import sys
input=sys.stdin.readline

T=int(input())

for i in range(T) :
    n=int(input())
    boards=[list(map(int, input().split())) for _ in range(2)]

    for j in range(1, n) :
        if j==1 :
            boards[0][j]+=boards[1][j-1]
            boards[1][j]+=boards[0][j-1]
        else:
            boards[0][j] += max(boards[1][j-1], boards[1][j-2])
            boards[1][j] +=max(boards[0][j-1], boards[0][j-2])
    print(max(boards[0][n-1], boards[1][n-1]))