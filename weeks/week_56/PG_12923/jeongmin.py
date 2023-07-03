# 해당 숫자의 약수 중에 자기 자신을 제외하고 가장 큰 수 구하기
def divisor(n):
    if n == 1:
        return 0

    block = 1
    for i in range(2, int(n**(1/2)+1)):
        if n % i == 0:
            # 1부터 10,000,000까지의 숫자가 적힌 블록 사용
            if n//i > 10000000:
                block = max(block, i)
                continue
            block = max(block, n//i)
    return block


def solution(begin, end):
    answer = []

    for x in range(begin, end+1):
        answer.append(divisor(x))

    return answer
