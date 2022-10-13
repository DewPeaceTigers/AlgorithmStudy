'''
시간초과 해결
https://velog.io/@ju_h2/Python-%EB%B0%B1%EC%A4%80-1092.-%EB%B0%B0-%ED%92%80%EC%9D%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%83%90%EC%9A%95-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EA%B7%B8%EB%A6%AC%EB%94%94-%EA%B5%AC%ED%98%84-5
'''
import sys
input=sys.stdin.readline
n=int(input())
crains=list(map(int, input().split()))
m=int(input())
boxs=list(map(int, input().split()))

crains.sort(reverse=True)
boxs.sort(reverse=True)
ans=0

if crains[0]<boxs[0]: #무게가 제일 많이 나가는 박스 무게가 크레인이 가능한 무게보다 큰 경우
    print(-1)
    exit()
else:
    while len(boxs)>0 :
        for crain in crains:
            for box in boxs:
                if crain>=box :
                    boxs.remove(box)
                    break
        ans+=1
    print(ans)
