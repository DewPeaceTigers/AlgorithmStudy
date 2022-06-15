import sys
input=sys.stdin.readline
docs=input().strip()
target=input().strip()
index=-1
found=[]
while True:
    index = docs.find(target, index + 1) # 모든 target 찾기 
    if index == -1: break
    if not found:
        found.append(index)
    elif found[-1]+len(target)<=index: # 찾으면서 겹치지 않게 찾아야 한다는 조건 만족시키기
        found.append(index)
print(len(found))


## others
# doc=input()
# word=input()

# index=0
# result=0
# while len(document)-index>=len(word):
#     if document[index:index+len(word)]==word:
#         result+=1
#         index+=len(word)
#     else:
#         index+=1
# print(result)