### 민지
1. 이진 탐색 알고리즘이란

    정렬된 리스트에서 검색 값을 찾아내는 알고리즘이다. 

2. 이진 탐색의 동작 과정 설명

    배열의 중간 값을 가져온 후 중간 값과 찾을 값을 비교한다. 찾을 값이 중간 값과 같으면 종료, 중간 값보다 크면 중간 값 기준으로 배열의 오른쪽 구간을 탐색, 중간 값보다 작으면 중간 값 기준으로 배열의 왼쪽 구간을 탐색하면 된다. 값을 찾거나 더 이상 배열이 남지 않을때까지 반복한다. 
3. 이진 탐색 알고리즘이 종료되는 조건 두가지

    - 검색 값을 찾은 경우
    - 더 이상 검색할 범위가 없을 경우

4. 이진 탐색 알고리즘 시간 복잡도

    O(log n)
5. 이진 탐색 알고리즘을 재귀함수로 구현한 코드의 빈칸 채우기
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

1)start>end
2)mid-1
3)mid+1