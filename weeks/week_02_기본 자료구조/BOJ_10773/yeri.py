K = int(input())
nums=[]
for _ in range(K):
    n = int(input())
    if n == 0: # 들어온 수가 0 일때
        nums.pop() # 가장 최근에 들어온 수가 담긴 nums의 top을 뺀다.
    else: # 아닐 경우
        nums.append(n) # nums에 넣는다.
print(sum(nums))