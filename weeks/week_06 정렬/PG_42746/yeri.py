"""
못품
%10==0인 것을 예외 처리하려고 했으나 경우의 수가 너무 많았다.
"""
def solution(numbers):
    numbers= list(map(str,numbers)) #[ str(n) for n in numbers]
    numbers.sort(reverse=True, key=lambda x:(x*3)) # 1000까지의 숫자들이니깐 세자리 수로 맞춰주고 비교하면 된다..

    return str(int(''.join(numbers)))