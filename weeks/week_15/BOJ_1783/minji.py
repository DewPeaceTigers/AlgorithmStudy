'''
무조건 오른쪽으로만 이동

1. 세로나 가로의 길이가 1이면 시작 칸만 가능
2. 세로의 길이가 2일 경우, 세로로 한칸만 이동하는 경우만 가능
4가지 경우로 다 이동 못하니까 최댓값 4
3. 가로의 길이가 6이하일 경우에, 4번 이상으로 움직인다고 하면, 1~4번 방법을 모두 써야 하므로 최댓값은 4가 될 것이고, 최소값은 자신 가로의 길이가 될 것이다.
4. 세로의 길이가 3 이상이고, 가로의 길이가 7이상인 경우에는 이동에 제약이 없으므로 오른쪽으로 두 칸을 가야만 하는 강제적인 방법을 빼고는 한칸씩만 움직이면 되므로 m-2 라는 값이 나오게 된다.
'''
n, m = map(int, input().split())
if n == 1:
    print(1)
elif n == 2:
    print(min(4, (m-1)//2+1))
elif m <= 6:
    print(min(4, m))
else:
    print(m-2)