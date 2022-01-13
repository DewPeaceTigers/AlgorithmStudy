T= int(input())
for i in range(T):
    num = list(map(int,input().split()))
    for j in range(3):
        max_n = max(num)
        num.remove(max_n)
    print(max_n)