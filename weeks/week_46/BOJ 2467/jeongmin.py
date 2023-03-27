import sys
input = sys.stdin.readline

n = int(input())
liquids = list(map(int, input().split()))

ans = float("INF")
ans_left = 0
ans_right = 0

for i in range(n-1):
    current = liquids[i]

    start = i + 1
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        tmp = current + liquids[mid]

        if abs(tmp) < ans:
            ans = abs(tmp)
            ans_left = i
            ans_right = mid

            if tmp == 0:
                break
        
        if tmp < 0:
            start = mid + 1
        
        else:
            end = mid - 1

print(liquids[ans_left], liquids[ans_right])