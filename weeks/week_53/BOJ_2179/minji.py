'''
어디가 잘못된건지 못찾겠움
'''
import sys

input=sys.stdin.readline

n=int(input())
words=[]
for i in range(n) :
    words.append([input().rstrip(), i])

sort_words=words[:]
sort_words.sort()
start, end=0, 1
maxLength=0
ans_idx=[0, 1]
ans=["", ""]

def check(a, b):
    cnt=0
    if a==b:
        return 0
    for i in range(min(len(a), len(b))) :
        if a[i]==b[i]:
            cnt+=1
        else:
            break
    return cnt

while start<end and start<n and end<n :
    length=check(sort_words[start][0], sort_words[end][0])
    if length==0 : #접두사 없는 경우
        start=end
        end+=1
    else:
        tmp1, tmp2=sort_words[start], sort_words[end]
        if tmp1[1]>tmp2[1] : #더 작은 인덱스
            tmp1, tmp2=tmp2, tmp1
        if length>maxLength: #접두사의 길이가 더 큰 경우
            ans_idx=[tmp1[1], tmp2[1]]
            maxLength=length
            ans=[tmp1[0], tmp2[0]]
        elif length==maxLength : #접두사의 길이가 같은 경우
            if ans_idx[0]>tmp1[1]:
                ans_idx=[tmp1[1], tmp2[1]]
                ans=[tmp1[0], tmp2[0]]
            elif ans_idx[0]==tmp1[1] and ans_idx[1]>tmp2[1]:
                ans_idx[1]=tmp2[1]
                ans[1]=tmp2[0]
        if end==n-1 :
            start+=1
        else:
            end+=1

print(ans[0])
print(ans[1])