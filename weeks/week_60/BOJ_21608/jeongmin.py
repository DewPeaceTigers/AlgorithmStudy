import sys
import heapq

input = sys.stdin.readline

N = int(input())

# 교실 정보
classes = [[0]*N for _ in range(N)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def boundaryCheck(r, c):
    global N
    if r < 0 or r >= N or c < 0 or c >= N:
        return False
    return True


# 좋아하는 학생 목록 저장
like_students = [[] for _ in range(N**2+1)]
for _ in range(N**2):
    nums = list(map(int, input().split()))
    like_students[nums[0]] = nums[1:]

    # 힙큐 구성
    # 좋아하는 학생 많은 순, 비어있는 칸 많은 순, 행*N+열 작은 순
    q = []

    for x in range(N):
        for y in range(N):
            # 비어있는 칸이 아니라면 넘어감
            if classes[x][y] != 0:
                continue

            # 좋아하는 친구 수, 빈칸 수
            like_cnt, blank_cnt = 0, 0

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if not boundaryCheck(nx, ny):
                    continue

                if classes[nx][ny] in like_students[nums[0]]:
                    like_cnt += 1

                if classes[nx][ny] == 0:
                    blank_cnt += 1

            heapq.heappush(q, (-like_cnt, -blank_cnt, x*N + y))

    # nums[0]번호 학생은 힙 큐에서 첫번째 원소에 해당하는 칸에 자리 잡음
    r, c = q[0][2]//N, q[0][2] % N
    classes[r][c] = nums[0]

# 학생의 만족도 총 합
answer = 0
for x in range(N):
    for y in range(N):
        # 칸에 있는 학생 번호
        num = classes[x][y]

        # 만족도 구하기
        satisfaction = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not boundaryCheck(nx, ny):
                continue

            if classes[nx][ny] in like_students[num]:
                satisfaction += 1

        if satisfaction > 0:
            answer += 10**(satisfaction-1)

print(answer)
