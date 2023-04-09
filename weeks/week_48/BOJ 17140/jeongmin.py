from collections import Counter

r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

# 인덱스이므로 -1 처리
r -= 1
c -= 1

# 연산의 최소 시간 저장
time = 0

# 100 이하일 동안 수행
while time <= 100:
    # A[r][c]에 들어있는 값이 k인 경우!
    if r < len(A) and c < len(A[0]) and A[r][c] == k:
        print(time)
        break

    # C연산인 경우 열 계산을 위해 A 변경
    C = False
    if len(A) < len(A[0]):
        C = True
        A = list(zip(*A))

    # 연산 수행
    max_len = 0
    tmp = []
    for cur in A:
        counter = Counter(cur)
        # 0은 무시하기
        if counter.get(0):
            del counter[0]
        cnt = list(map(list, counter.items()))
        # 등장 횟수 오름차순, 숫자 오름차순
        cnt.sort(key=lambda x: (x[1], x[0]))
        # sum(cnt, [])
        # [[2, 1], [1, 2]] -> [2, 1, 1, 2] 로 변환
        tmp.append(list(sum(cnt, []))[:100])  # 100개 넘어가면 나머지 버리기
        max_len = max(max_len, len(tmp[-1]))

    for i in range(len(tmp)):
        if len(tmp[i]) < max_len:
            # 0 채우기
            tmp[i] += [0]*(max_len-len(tmp[i]))

    A = tmp

    # C연산인 경우 다시 원래 형태로
    if C:
        A = list(zip(*A))
    time += 1

if time > 100:
    print(-1)
