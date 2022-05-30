import sys

input = sys.stdin.readline

N = int(input())

# 사자를 배치하는 경우
# 1) 첫번째 열, 2) 두번째 열, 3) 배치 X
cage = [[1, 1, 1] for _ in range(N)]

for i in range(1, N):
    # 첫번째 열 : 윗 줄 두번째 열 + 배치 X
    cage[i][0] = (cage[i-1][1]+cage[i-1][2]) % 9901

    # 두번째 열 : 윗 줄 첫번째 열 + 배치 X
    cage[i][1] = (cage[i-1][0]+cage[i-1][2]) % 9901

    # 배치 X : 윗 줄 첫번째 열 + 두번째 열 + 배치 X
    cage[i][2] = (cage[i-1][0]+cage[i-1][1]+cage[i-1][2]) % 9901

print(sum(cage[N-1]) % 9901)