import sys

# 해당 숫자 이상의 수 중 가장 가까운 인덱스를 리턴하는 함수 ( 정렬이 되어있을 때만 가능 )
def lower_bound(s, e, v):
    while s < e:
        m = (s + e) // 2
        if res[m] < v:
            s = m + 1
        else:
            e = m
    return e


n = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().split()))
res = []

for i in range(n):
    if i == 0:  # 첫 번째 수는 res에 추가
        res.append(line[0])
    if res[-1] < line[i]:   # line[i]가 res의 마지막 요소보다 크면 마지막에 추가
        res.append(line[i])
    else:   # line[i]가 res의 마지막 요소보다 작으면 lower bound 하여 나온 index위치의 값과 교환
        tmp = lower_bound(0, len(res), line[i])
        res[tmp] = line[i]


print(n - len(res))