T = int(input())

for i in range(T):
    x, y = map(int, input().split())
    distance = y - x
    n = 0

    while True:
        if distance <= n * (n + 1):
            break
        n += 1

    if distance <= n ** 2:
        print(n * 2 - 1)
    else:
        print(n * 2)