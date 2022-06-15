1.  이진탐색의 조건은?

    정렬된 데이터를 탐색해야 한다.

2.  순차탐색과 이진탐색의 시간복잡도는?

    - 순차 탐색 : O(n)
    - 이진 탐색 : O(logn)

3.  이진탐색의 동작과정을 설명해주세요.

    1. 중간 값을 찾는다.
    2. 중간 값이랑 찾고자 하는 값을 비교한다.
       1. 같을 경우 반환한다.
       2. 클 경우 중간값 기준 왼쪽을 탐색한다.
       3. 작을 경우 중간값 기준 오른쪽을 탐색한다.
    3. 1개 남을 때까지 반복한다.

4.  재귀함수를 이용하여 이진탐색을 구현한 코드입니다. 빈칸을 채워주세요!

    ```python
    def binary_search(array, target, start, end) :
      # 종료조건
      ________________
      ________________
      mid = (start+end)//2

      if ________________ :
        return mid

      elif target < array[mid] :
        return binary_search(array, target, _____, _____)
      else :
        return binary_search(array, target, _____, _____)
    ```

    1. `if start > end :`
    2. `return none`
    3. `target == array[mid]`
    4. `start`, `mid-1`
    5. `mid+1`, `end`

5.  이진 탐색을 쉽게 구현할 수 있도록 파이썬에서 제공하는 라이브러리는?  
    그리고 해당 라이브러리에서 가장 많이 사용되는 메소드(2가지)는?

        bisect
        - bisect_left()
        - bisect_right()

6.  이진탐색은 \_\_\_된 자료구조를 바탕으로 한다.

    정렬

7.  이진 탐색은 반복 구조로 구현할 수 있다. 아래 빈칸에 들어갈 코드를 작성하세용

    ```python
    def binary_search():
    left,right=0,len(nums)-1
    while ________ :
    	mid=(left+right)//2
        if nums[mid]<target:
        	left=mid+1
        elif nums[mid]>target:
        	right=mid-1
        else:
        	return mid
    return -1
    ```

    `left <= right`

8.  이진 탐색은 **\_** 알고리즘을 응용한 것이다.

    분할 정복

9.  이진 탐색 알고리즘이란

    반 씩 나누어서 탐색하는 알고리즘

10. 이진 탐색 알고리즘이 종료되는 조건 두가지

- 값을 찾은 경우
- 값을 못찾았지만 배열의 개수가 하나 남은 경우

11. 이진 탐색 알고리즘을 재귀함수로 구현한 코드의 빈칸 채우기

```python
def binary_search(target, start, end, data) :
    if 1)________________ :
        return -1
    mid=(start+end)//2
    if data[mid] == target :
        return mid
    elif data[mid] > target:
        end = 2)_____
    elif data[mid] < target:
        start = 3)______
    return binary_search(target, start, end, data)
data=[16, 20, 33, 46, 57, 66, 78, 87, 96]
target=33
index=binary_search(target, 0, len(data)-1, data)
print(index)
```

    1) `start>end`
    2) `mid-1`
    3) `mid+1`
