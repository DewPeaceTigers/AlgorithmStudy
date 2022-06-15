def solution(brown, yellow):
    bxy=(brown-4)//2 # brown에서 모든 모서리 부분의 사각형을 제외하고 나누기 2를 한 몫은 yellow의 가로, 세로를 더한 거랑 마찬가지이다.
    for i in range(1,(bxy//2)+1): # 1부터 돌면서 bxy와 i의 관계 속에 이 둘을 곱했을 때 yellow의 너비, 즉 가로*세로랑 같으니 그게 같으면 해당 것을 작은 것부터 반환하면 된다.
        if i*(bxy-i)==yellow:
            return [bxy-i+2,i+2]

# def solution(brown, red):
#     for i in range(1, int(red**(1/2))+1):
#         if red % i == 0:
#             if 2*(i + red//i) == brown-4:
#                 return [red//i+2, i+2]