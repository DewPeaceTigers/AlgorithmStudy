def solution(number, k):
    answer = ''

    nums = []

    for n in number:
        while nums and nums[-1] < n and k > 0:
            nums.pop()
            k -= 1

        nums.append(n)

    # k의 개수가 남은 경우 뒤쪽 k개 수 제거
    if k > 0:
        nums = nums[:-k]

    answer = "".join(nums)

    return answer
