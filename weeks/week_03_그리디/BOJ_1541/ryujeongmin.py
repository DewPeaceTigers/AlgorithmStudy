''' [풀이]
1. 정규표현식을 활용해 문자열에서 숫자, 부호 리스트에 각각 저장
2. 부호 개수만큼 반복문 수행
  - sum 변수를 이용해 괄호 영역 합 구하기
  - 부호가 +, - 밖에 없으므로 -가 나오면 ans에서 sum만큼 빼주고 -부호 다음 숫자부터 괄호 연다! 
    (다음 뺄셈 부호가 나오기 전까지 괄호 영역으로 더해줌.) 
  - + 부호가 나온 경우
    - sum이 0이 아닐 때 : sum에 더해준다.
    - sum이 0일 때 : 앞에 -부호가 없다는 의미이므로 그 숫자는 ans에 더해준다.
3. 반복문이 끝났는데 sum 값이 남아있는 경우 마저 빼준다.
'''

import re # 정규표현식 사용
import sys
input = sys.stdin.readline

p_num = re.compile('\d{1,5}') # 숫자 0~9 (5자리까지)
p_sign= re.compile('[+-]')  # 부호 (+,-)

# 식 입력
expression = input()

# 숫자, 부호 각각 리스트에 저장
nums = list(map(int, p_num.findall(expression)))
signs = p_sign.findall(expression)

ans = nums[0] # 답 저장(초기값: 첫번째 숫자)
sum = 0 # 뺄셈 괄호 영역 합

for i in range(len(signs)):
  # 부호가 음수면
  if signs[i] == '-':
    ans-= sum # sum 만큼 빼기
    sum= nums[i+1] # sum에 num[i+1] 대입
  else:
    if sum:
      sum += nums[i+1] # 뺄셈 괄호 영역 값으로 더해줌
    else:
      ans +=nums[i+1] # 더하기 (앞에 뺄셈 부호 없음..)

# sum에 값이 남아있으면 그 값 마저 빼주기
if sum:
  ans -= sum

print(ans)