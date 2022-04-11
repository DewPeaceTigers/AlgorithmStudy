def distnace(x,y,tx,ty):
    return abs(x-tx)+abs(y-ty)
def solution(places):
    answer = []
    for place in places:
        temps=[]
        ans=1
        for p in place:
            temps.append(list(p))
        students=[]
        for i,temp in enumerate(temps):
            for j,t in enumerate(temp):
                if t == 'P': students.append([i,j])
        while students:
            x,y = students.pop()
            for tx,ty in students:
                quarantined=True
                dis= distnace(x,y,tx,ty)
                if dis==1:
                    quarantined=False
                elif dis==2:
                    mx=(tx-x); my=(ty-y);
                    if abs(mx)==2 or abs(my)==2:
                        if temps[x + (mx//2)][y + (my//2)] != 'X':
                            quarantined = False
                    elif abs(mx)==1 or abs(my)==1:
                        if not (temps[x][ty]=='X' and temps[tx][y]=='X'):
                            quarantined=False
                if not quarantined:
                    ans=0
                    break
        answer.append(ans)
    return answer