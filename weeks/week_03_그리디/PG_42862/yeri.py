def solution(n, lost, reserve):
    lost.sort() # 순서대로 차례로 해야함
    reserve.sort()
    for l in lost:
        n -= 1
        if l in reserve:  # 잃어버렸지만 여분이 있음
            n += 1
        # 이 아래 -> 잃어버렸고, 여분도 없음
        elif l - 1 in reserve and l - 1 not in lost:
            # 잃어버린 번호 앞번호가 빌려줄 수 있다. 그치만 잃어버린 애가 아니어야 함
            n += 1
            reserve.remove(l - 1)  # 빌려줌
        elif l + 1 in reserve and l + 1 not in lost:
            # 잃어버린 번호 뒷번호가 빌려줄 수 있다. 그치만 잃어버린 애가 아니어야 함
            n += 1
            reserve.remove(l + 1)  # 빌려줌

    return n