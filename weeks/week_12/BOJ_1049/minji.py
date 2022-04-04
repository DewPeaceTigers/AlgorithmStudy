'''
꼭 개수 맞춰서 구매할 필요 없음
패키지로만 사는 경우
낱개로만 사는 경우
패키지+낱개로 사는 경우
3가지 경우 중 최소값출력ㅇ
'''
import sys

n, m=map(int, sys.stdin.readline().split())

package_cost=[]
piece_cost=[]
for i in range(m) :
    p, c=map(int, sys.stdin.readline().split())
    package_cost.append(p)
    piece_cost.append(c)

package_cost.sort()
piece_cost.sort()
package=n//6
piece=n%6
money1=package_cost[0]*(package+1)
money2=package_cost[0]*package+piece_cost[0]*piece
money3=piece_cost[0]*n
print(min(money3, money2, money1))
