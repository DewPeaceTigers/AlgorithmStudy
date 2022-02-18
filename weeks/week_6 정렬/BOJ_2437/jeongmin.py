'''[풀이] 못 푼 문제.. 결국 답 찾아봄!
리스트를 오름차순으로 정렬해주고 하나씩 더하면서 해당 수를 리스트의 다음 요소(다음 추)와 비교
비교해서 다음 추가 그동안 더했던 추들의 합보다 더 크다면 해당 값은 주어진 N개의 추들로 만들 수 없음.
'''

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split())
arr.sort() # 리스트를 오름차순으로 정렬

target =1
for x in arr:
	if target<x: # target보다 다음 추가 더 큰 경우
		break
	target+=i # 하나씩 더하기

print(target)