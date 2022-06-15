''' [풀이]
배열 A 에서 3번째 큰 값 출력
    - 배열 A 입력, 내림차순 정렬, A[2] 출력 
 or - 배열 A 입력, 오름차순 정렬, A[-3] 출력
'''

#  테스트 케이스의 개수 T(1 ≤ T ≤ 1,000) 입력
T = int(input())

for i in range(T):
  # 배열 A 입력, 내림차순 정렬
  A = sorted(list(map(int, input().split())), reverse=True)

  # N 번째 큰 수 출력 (N은 항상 3)
  print(A[2])