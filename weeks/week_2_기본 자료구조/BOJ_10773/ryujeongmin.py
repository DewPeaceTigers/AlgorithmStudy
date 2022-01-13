''' [풀이]
스택의 기본적인 연산 (리스트 사용)
    - 정수 x가 0이 아닐때 : append(x)
    - 정수 x가 0일때 : pop()
    
정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장할 수 있으므로
pop() 연산 시 스택이 비어있는지 확인할 필요가 없음
'''

# 정수 K (1 ≤ K ≤ 100,000) 입력
K = int(input())

# 스택 사용
stack=[]

# K개 수 입력
for _ in range(K):
  n = int(input())

  # n이 0이 아니라면 스택 push
  if n:
    stack.append(n)
  # n이 0이라면 스택 pop
  else:
    stack.pop()
  
print(sum(stack))