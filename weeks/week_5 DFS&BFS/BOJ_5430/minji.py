'''
R마다 reverse()함수 실행시 시간 초과
n==0일때 error를 출력해버리면 명령이 R만 있을 때  오류
'''

import sys
from collections import deque

T=int(sys.stdin.readline())

for i in range(T) :
    command=sys.stdin.readline()
    n=int(sys.stdin.readline())
    arr=sys.stdin.readline().rstrip()[1:-1].split(",")

    queue=deque(arr)

    r_count=0 #Reverse 횟수(홀수->뒤집음 짝수->그대로)
    error=False #error인 경우

    if n == 0 :#아무것도 없을때
        queue=[] #error값을 변경하면 R명령만 할때도 error출력

    for j in command :
        if j == 'R' : #R 횟수가 홀수이면 수행 짝수이면 수행 x
            r_count+=1
        elif j == 'D' :
            if len(queue) == 0 :
                error=True
                break
            if r_count%2==0: #짝수이면 앞에를 삭제
                queue.popleft()
            else : #홀수이면 뒤를 삭제
                queue.pop()

    if r_count%2==1:
        queue.reverse()
    if error==False :
        print("["+",".join(queue)+"]")
    else:
        print("error")
