def solution(prices):
    answer = [0] * len(prices)

    stack = []
    for i, price in enumerate(prices):
        # 가격이 떨어지는 경우
        while stack and price < stack[-1][0]:
            p, idx = stack.pop()
            # i-idx 초 후에 가격이 떨어짐
            answer[idx] = i - idx
        stack.append((price, i))  # 스택에 [가격, 현재 시점] 추가

    # 끝까지 가격이 떨어지지 않는 경우
    for p, idx in stack:
        answer[idx] = len(prices) - 1 - idx

    return answer