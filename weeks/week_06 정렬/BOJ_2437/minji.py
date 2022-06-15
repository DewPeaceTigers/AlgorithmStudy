'''
풀이 참고했는데,, 왜 이렇게 하면 답이 나오는지 모르겠움,,
'''
n=int(input())
weight=list(map(int, input().split()))
weight.sort()

result=weight[0]
for i in range(n) :
    if result < weight[i] :
        break
    result+=weight[i]
print(result)