def solution(n):
    return format(n,'b').count(1)
# def solution(n):
#     ans=1
#     while n>1:
#         ans+=n%2
#         n=n//2
#     return ans
"""
 n 위치에서 0으로 갈 때 순간이동이 가능하지 못한 순간에 1칸씩만 점프를 뛰면 되는데,
 이 과정이 주어진 수를 이진화 했을 때 1의 개수를 구하는 과정과 동일한 것을 확인했습니다.
 점프(Shift 연산), 이동 (1의 자리수의 0 -> 1 변환) => 2진표현( 점프 및 이동의 기록 )
 5 -> 1 4 -> 1 2
 6 -> 1 1 -> 3 
 5000 -> 2500 -> 1250 -> 625 -> 624 +1 -> 312 +1 -> 156 + 1 -> 78 +1 -> 39 +1
 -> 19 +1 +1 -> 9 + 1 +1 +1 -> 4 +1 +1 +1 +1 -> 2 +1 +1 +1 +1 -> 1 + 1 + 1 + 1 + 1
"""