import sys

input = sys.stdin.readline

A, B = input().split()
a, b = int(A), int(B)

# 거꾸로 생각하기
# B에서 거꾸로 가면 A가 나오는지
count = 1
while b > a:
    # print(a, b, B, count)
    # 짝수이면 나누기 2
    if b%2 == 0:
        b //= 2
        B = str(b)

    # 끝에가 1이면 마지막 1 제거
    elif B[-1] == '1':
        B = B[:-1]
        b = int(B)

    # 짝수도 아니고 끝이 1이 아니라면 불가능
    else:
        break

    count+=1

answer = count if a==b else -1
print(answer)