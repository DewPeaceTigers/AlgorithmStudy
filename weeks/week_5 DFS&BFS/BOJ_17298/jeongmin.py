'''시간초과,, 결국 답 찾아봄'''
'''[풀이] 
스택을 사용해야 시간 복잡도가 줄어든다.

반복문 ( 0 ~ N-1 )
  1. stack에 값이 있고 A[top]과 A[i] 값을 비교
  2. 오큰수를 만족한다면 stack.pop()
      answer[stack.pop()]에 A[i] 값 대입
  3. 수열 A에서 인덱스를 stack에 저장한다.
'''

import sys
input=sys.stdin.readline

# 수열 A의 크기 N (1 ≤ N ≤ 1,000,000) 입력
N = int(input())

# 수열 A 입력
A = list(map(int, input().split()))

# 오큰수를 못 찾은(오른쪽의 수들보다 큰) 값들의 인덱스를 스택에 저장
stack=[]

# NGE 저장
answer=[-1]*N

for i in range(N):
  # A[stack의 top]과 A[i]값 비교 -> 오큰수가 되는지 확인
  while stack and A[stack[-1]]<A[i]:
    # 오큰수를 만족한다면 stack.pop()
    answer[stack.pop()] = A[i]
  stack.append(i)

print(*answer)