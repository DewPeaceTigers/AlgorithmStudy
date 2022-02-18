n=int(input())
ph=list(map(int, input().split()))
ph.sort()
left,right=0, n-1
_min=abs(ph[left]+ph[right])
ans=[ph[left], ph[right]]
while left<right :
    tmp=ph[left]+ph[right]
    if abs(tmp) < _min :
        _min=abs(tmp)
        ans=[ph[left], ph[right]]
        if _min==0 : #두 용액의 합이 0이면 최솟값이니까 종료
            break
    if tmp < 0 : #두 용액의 합이 0보다 작으면 음수인 용액을 더 큰 값으로 바꿔서 0에 가까워지도록
        left+=1
    else: #두 용액의 합이 0보다 크면 양수인 용액을 더 작은 값으로 바꿔서 0에 가까워지도록
        right-=1
print(ans[0], ans[1])