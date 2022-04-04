'''
양수끼리 곱셈
음수끼리 곱셈
0과 음수 곱
1은 덧셈

'''

import sys

n=int(input())
positive=[]
negative=[]
one=[]
for i in range(n) :
    num=int(sys.stdin.readline())
    if num>1:
        positive.append(num)
    elif num<=0 :
        negative.append(num)
    else:
        one.append(num)

positive.sort(reverse=True)
negative.sort()
ans=0
if len(positive)%2==0 :
    for i in range(0, len(positive)-1, 2) :
        ans+=positive[i]*positive[i+1]
else:
    for i in range(0, len(positive)-1, 2) :
        ans+=positive[i]*positive[i+1]
    ans+=positive[-1]

if len(negative)%2==0 :
    for i in range(0, len(negative)-1, 2) :
        ans+=negative[i]*negative[i+1]
else:
    for i in range(0, len(negative)-1, 2) :
        ans+=negative[i]*negative[i+1]
    ans+=negative[-1]

ans+=len(one)
print(ans)