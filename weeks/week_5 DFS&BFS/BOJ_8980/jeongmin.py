'''[풀이]
무엇을 기준으로 해야할지 모르겠어서.. 결국 답 참고
https://javaiyagi.tistory.com/586

그리디, 정렬
1. 도착점만을 기준으로 정렬을 해야한다.
2. 각 박스를 실었을 때 트럭에 남은 적재량 저장
3. 정렬된 리스트를 순회하며 배송을 받기 전 마을의 수용 가능한 개수와 
현재 마을에서 실을 개수 중 작은 값을 구하여 결과에 더한다. 

'''

import sys
input = sys.stdin.readline

# 마을 수 N과 트럭의 용량 C 입력
N, C = map(int, input().split())

# 보내는 박스 정보의 개수 M 입력
M = int(input())

box=[]

for _ in range(M):
  # 박스를 보내는 마을번호, 박스를 받는 마을번호, 보내는 박스 개수(1이상 10,000이하 정수)를 나타내는 양의 정수 입력
  box.append(list(map(int, input().split())))

box.sort(key=lambda x: [x[1]])

answer = 0  # 최대 박스 수

remain = [C] * (N + 1)  # 각 위치에 남은 공간

for i in range(M):
    _min = C  # C개를 옮길 수 있다고 가정

    # 시작마을~도착마을 중 remain 최소값(_min)
    for j in range(box[i][0], box[i][1]):
        _min = min(_min, remain[j])

    # _min과 실을 박스 중 작은 값
    _min = min(_min, box[i][2])

    for j in range(box[i][0], box[i][1]):
        remain[j] -= _min
    answer += _min

print(answer)