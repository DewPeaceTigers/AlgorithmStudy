import sys

input = sys.stdin.readline

in_str = input().rstrip()
bomb = input().rstrip() # 폭발 문자열 입력
l = len(bomb)   # 폭발 문자열 길이
stack = []

for x in in_str:
    # 스택에 문자 추가
    stack.append(x)

    # 뒤에서부터 l개의 문자를 합친 문자열이 폭발문자열과 같다면
    if len(stack)>=l and ''.join(stack[len(stack)-l:]) == bomb:
        # 스택에서 l개 문자 제거
        for i in range(l):
            stack.pop()

print(''.join(stack) if len(stack)>0 else "FRULA")
