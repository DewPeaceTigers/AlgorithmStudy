"""
시간 소요가 됨.
모르겠으면 예시 잘 분석하기
"""
from collections import deque
def solution(numbers):
    ans=[]
    for num in numbers:
        binary = deque(format(num,'b'))
        if num%2!=0: binary.appendleft('0')
        for i in range(len(binary)-1,-1,-1):
            # 짝수일 때, 가장 뒤에 있는 0을 1로
            # 홀수일 때, 가장 뒤에 있는 0을 1로, 그 앞의 인덱스를 0으로
            if binary[i]=='0':
                binary[i]='1'
                if num%2!=0:
                    binary[i+1]='0'
                break
            if i == 0:
                binary.append('0')
        ans.append(int(''.join(binary),2))
    return ans