"""
큰거끼리 곱하면 가장 큰 합을 찾을 수 있다.
대신 양수는 양수끼리 음수는 음수끼리 곱해줘야 한다.
각각 모으고 내림차순으로 정렬을 해준다.
양수는 1*1보다 1+1이 더 낫다.
0은 음수끼리에 포함시킨다.
"""
import sys
input = sys.stdin.readline
n = int(input())
even = []
odd = []
for _ in range(n):
    temp = int(input())
    if temp > 0 : even.append(temp)
    else : odd.append(temp)
        
even.sort(reverse=True)
odd.sort(reverse=True, key=lambda x:-x)
        
def add(list):
    sum=0
    length=len(list)
    grouped=[False]*length
    for i in range(length):
        if grouped[i]: continue
        if i == length - 1:
            sum += list[i]
        elif sum + list[i] > sum + (list[i] * list[i + 1]):
            sum += list[i]
        elif sum + list[i] == sum + (list[i] * list[i + 1]):
            if sum + list[i] + list[i + 1] > sum + (list[i] * list[i + 1]):
                sum += list[i] + list[i + 1]
                grouped[i + 1] = True
            else:
                sum += (list[i] * list[i + 1])
                grouped[i] = True
                grouped[i + 1] = True
        else:
            sum += (list[i] * list[i + 1])
            grouped[i] = True
            grouped[i + 1] = True
    return sum

print(add(even)+add(odd))