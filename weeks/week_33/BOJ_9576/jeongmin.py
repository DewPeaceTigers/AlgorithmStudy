import sys

input = sys.stdin.readline

T = int(input())

for t in range(T):
    N, M = map(int, input().split())

    students = [list(map(int, input().split())) for _ in range(M)]

    students.sort(key=lambda x: [x[1]])

    check = [False] * (N+1)

    answer = 0
    for i in range(M):
        for x in range(students[i][0], students[i][1]+1):
            if not check[x]:
                answer += 1
                check[x] = True
                break
    print(answer)