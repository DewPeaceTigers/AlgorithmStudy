n = int(input())
answer = 0
money = []
for i in range(n):
    k = int(input())
    money.append(k)
    if k == 0:
        answer -= money.pop()
    else :
        answer += k

print(answer)