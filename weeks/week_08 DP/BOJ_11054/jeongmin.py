'''[풀이] 정답 찾아봄..
- 각 인덱스별로 증가하는 수열 길이 + 감소하는 수열 길이의 합 구하기
- 길이의 합 중 최댓값 구하기
'''

import sys
input= sys.stdin.readline

# N 입력(1 ≤ N ≤ 100)
N = int(input())

case = list(map(int, input().split()))
reverse_case = case[::-1]

increase = [1 for i in range(N)] # 가장 긴 증가하는 부분 수열
decrease = [1 for i in range(N)] # 가장 긴 감소하는 부분 수열(reversed)

for i in range(N):
    for j in range(i):
        if case[i] > case[j]:
            increase[i] = max(increase[i], increase[j]+1)
        if reverse_case[i] > reverse_case[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

result = [0 for i in range(N)]
for i in range(N):
    result[i] = increase[i] + decrease[N-i-1] -1

print(max(result))