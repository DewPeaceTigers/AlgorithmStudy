import sys


def check(s):
    for i in range(1, (len(s) // 2) + 1):
        leng = i
        start = 0
        start2 = start + i
        for j in range(len(s) - (leng * 2) + 1):
            if s[start + j:start + j + leng] == s[start2 + j:start2 + j + leng]:
                return False
    return True


def make_num(number, N):
    if check(number) is False:
        return
    if len(number) == N:
        print(number)
        sys.exit()

    else:
        for j in range(1, 4):
            make_num(number + str(j), N)


N = int(input())
make_num('1', N)