'''
길이가 최대 7이므로 순열 이용 가능
순열을 이용해서 가능한 숫자 조합을 배열에 저장
조합을 한 숫자들이 소수인지 판단 후에 결과 출력

'''
import itertools
import math


def isPrime(prime):
    if prime == 0 or prime == 1:
        return False
    for i in range(2, int(math.sqrt(prime)) + 1):
        if prime % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    num = list(map(int, numbers))
    check = True
    prime_num = []
    for i in range(1, len(numbers) + 1):  # 가능한 조합을 arr 배열에 저장
        arr = list(itertools.permutations(num, i))
        for j in range(len(arr)):  # 문자열->숫자
            prime = int(''.join(map(str, arr[j])))
            check = isPrime(prime)
            if check == True:
                prime_num.append(prime)

    return len(set(prime_num))