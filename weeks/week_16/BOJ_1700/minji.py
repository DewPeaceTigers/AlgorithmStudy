n, k=map(int, input().split())
use=list(map(int, input().split()))

plugs=[] #현재 콘센트에 있는 플러그
ans=0

for i in range(k) :
    if use[i] in plugs :
        continue
    if len(plugs)<n :
        plugs.append(use[i])
        continue

    temp=0
    pos=0
    for plug in plugs :
        if plug not in use[i:] : #현재 꽂혀있는 플러그가 뒤에 사용 안되면
            #다른 걸 끼우기 위해 빼야함
            temp=plug
            break
        elif use[i:].index(plug)>pos: #뒤에 사용될 플러그 위치
            pos=use[i:].index(plug)
            temp=plug
    #temp 빼야함
    plugs[plugs.index(temp)]=use[i]
    ans+=1
print(ans)

