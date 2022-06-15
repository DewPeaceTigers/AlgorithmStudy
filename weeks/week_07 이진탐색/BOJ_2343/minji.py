'''
블루레이 크기에 따라서 강의들을 차례차례 더해보고 크기 넘어갈때마다 블루레이 개수를 +1씩
'''
N, M=map(int, input().split())
lesson=list(map(int, input().split()))
start=max(lesson)
end=sum(lesson)
while start<=end:
    mid=(start+end)//2

    count=0
    time=0
    for l in lesson:
        if time+l>mid:
            count+=1
            time=l
        else:
            time+=l
    if time :
        count+=1

    if count<=M :
        end=mid-1
    else:
        start=mid+1
print(start)

