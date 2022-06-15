# 시간 초과 t1,t2
# def dfs(cnt,ops,numbers,target):
#     global count
#     if len(numbers)==cnt:
#         tmp=''
#         for n in range(len(numbers)):
#             tmp+=ops[n]+str(numbers[n])
#         if eval(tmp)==target:
#             count+=1
#         return
#     ops.append('+')
#     dfs(cnt+1,ops,numbers,target)
#     ops[-1]='-'
#     dfs(cnt+1,ops,numbers,target)
#     ops.pop()
# def solution(numbers, target):
#     global count
#     count = 0
#     dfs(0,[],numbers,target)
#     return count

## eval 이 시간이 오래 걸리는 것 같다.
def dfs(i,sum,target,numbers):
    if i==len(numbers):
        if sum==target:
            return 1
        return 0
    return dfs(i+1,sum+numbers[i],target,numbers)+dfs(i+1,sum-numbers[i],target,numbers)
def solution(numbers, target):
    count=dfs(1,numbers[0],target,numbers)+dfs(1,-numbers[0],target,numbers) # 두 가지만 있으므로 두개로 나뉘어서 시도해본다
    return count