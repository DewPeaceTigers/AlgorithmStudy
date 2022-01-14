''' [풀이]
스택을 이용
1. 괄호열을 하나씩 확인하면서 (, [ 인 경우 스택에 추가
2. ), ] 인 경우, 스택에서 pop 한 값 확인
  - 쌍을 이루지 않는다면 올바르지 않은 괄호열
  - 쌍을 이룬다면 바로 전 괄호열 값 확인
    - ( , [ 일 경우 : tmp 값 ans에 더하고 tmp 나누기
    - ), ] 일 경우 : tmp 나누기
3) 생각하지 못했던 반례!!
  - 반복문을 돌고 나서 스택에 값이 남아있는 경우, ex: ([]
'''
# 괄호열 입력
brackets= input()

# 스택 
stack=[]
tmp, ans = 1, 0

brackets_dic = {')':'(', ']':'['}

# 괄호열 하나씩 확인
for i, b in enumerate(brackets):
  # (, [ 인 경우 스택에 추가
  if b=='(' or b=='[':
    stack.append(b)
    if b=='(': tmp *=2
    elif b=='[': tmp *=3
  else:
    # 스택에 값이 있는 경우
    if stack:
      top = stack.pop()
      # 쌍을 이루지 않는 다면
      if brackets_dic[b]!= top:
        ans=0
        break
      # 쌍을 이룬다면
      else:
        # 바로 전 괄호열 확인
        if brackets[i-1] in ('[','('): ans += tmp
      
        if b==')': tmp//=2
        if b==']': tmp//=3
    else:
      ans =0
      break

# 스택에 괄호열이 남아있는 경우 - 올바르지 않은 괄호열
if stack:
  ans=0
  
print(ans)