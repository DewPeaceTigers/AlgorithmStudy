n=int(input())
def is_available(candidate, current_col):
    current_row = len(candidate)
    for queen_row in range(current_row):
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            # 수직 체크 : 같은 열에 있는지 없는지 / 대각선 체크 : 열 차이와 행 차이가 같으면 대각선에 위치한 것임
            return False
    return True


def DFS(N, current_row, current_candidate, final_result):
    if current_row == N: # n 행에 모든 queen을 찾았을 때
        final_result.append(current_candidate[:]) # [:] 얕은 복사
        return

    for candidate_col in range(N):
        if is_available(current_candidate, candidate_col): # 현재 행의 한 칸이 괜찮은지
            current_candidate.append(candidate_col) # 괜찮으므로 후보에 추가하고
            DFS(N, current_row + 1, current_candidate, final_result) # 다음 행으로 넘어가기
            current_candidate.pop() # 방금 후보 지우기


def solve_n_queens(N):
    final_result = []
    DFS(N, 0, [], final_result)
    return len(final_result)

print(solve_n_queens(n))

