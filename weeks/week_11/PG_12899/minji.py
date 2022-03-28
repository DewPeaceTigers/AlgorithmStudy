'''
나머지 1:1, 2:2 0:4
n을 3으로 나누면서 나머지를 저장하고
몫을 다시 3으로 나누는 걸 반복
'''


def solution(n):
    answer = ''
    while n > 0:
        if n % 3 == 0: #나머지가 0이면 4
            answer += '4'
            n = n // 3 - 1
        else:
            answer += str(n % 3)
            n //= 3

    return answer[::-1] #거꾸로 출력