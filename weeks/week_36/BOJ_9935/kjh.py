string=input()
target=input()
target_len=len(target)
stack=[]

for i in range(len(string)):
    stack.append(string[i])
    if ''.join(stack[-target_len:]) == target:
        for _ in range(target_len):
            stack.pop()
print(''.join(stack)) if len(stack) else print('FRULA')