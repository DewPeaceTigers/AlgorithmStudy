'''
N: 가지고 있는 숫자 카드의 개수
data: 숫자 카드에 적혀있는 정수
check: 몇개 가지고 있는지 구해야할 정수
binary_search(): 재귀함수로 구하며 몇개 갖고 있는지 구함
'''
'''

시간 초과 뜸;;

def binary_search(target, start, end, data) :
    if start > end :
        return 0
    mid=(start+end)//2
    if data[mid]==target :
        return data[start:end+1].count(target)
    elif data[mid]<target:
        return binary_search(target, mid+1, end, data)
    else:
        return binary_search(target, start, mid-1, data)
N=int(input())
data=list(map(int, input().split()))
M=int(input())
check=list(map(int, input().split()))
data.sort()
for i in check :
    start, end=0, len(data)-1
    if i is not None:
        count=binary_search(i, start, end, data)
        print(count, end=' ')
    else:
        print(0, end=' ')
'''
