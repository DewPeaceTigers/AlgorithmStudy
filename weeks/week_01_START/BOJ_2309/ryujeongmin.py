''' [풀이]
1. 이중 반복문 사용하여 아홉 난쟁이 중 일곱 난쟁이를 선택하는 모든 경우 확인
2. 일곱 난쟁이의 키의 합이 100이면 리스트에서 선택되지 않는 두 난쟁이 제거
3. 일곱 난쟁이의 키 오름차순 정렬
'''

# 일곱 난쟁이 찾기 
def find_dwarf(h):
  sum_h = sum(h)

  # 아홉 난쟁이 중 일곱 난쟁이 선택
  for i in range(8):
    for j in range(i+1, 9):
      # 일곱 난쟁이의 키의 합이 100이면
      if sum_h-(h[i]+h[j])==100:
        d1, d2 = h[i], h[j]
        # 두 난쟁이 제외
        h.remove(d1) 
        h.remove(d2)
        
        # 일곱 난쟁이의 키 오름차순 정렬 
        h.sort()
        return h
      
# 아홉 난쟁이의 키 입력
h = [ int(input()) for i in range(9)]

result = find_dwarf(h)

for x in result:
  print(x)