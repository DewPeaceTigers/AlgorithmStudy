import sys
input = sys.stdin.readline
n=int(input())
people=[]
for i in range(n):
    num,name=map(str,input().split())
    people.append([int(num),i,name]) # 가입한 순서도 저장.
people.sort() # 첫 번째 배열인 나이가 같다면 두 번째 배열을 비교하게 된다.
for num,i,name in people:
    print(num,name)