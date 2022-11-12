str=input()
bomb=input()
stack=[]
for s in str:
    stack.append(s)
    if ''.join(stack[-len(bomb):])==bomb :
        del stack[-len(bomb):]

if len(stack)==0:
    print("FRULA")
else:
    print(''.join(stack))

