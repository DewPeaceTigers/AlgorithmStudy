### 민지
1. 이진 탐색 알고리즘이란

2. 이진 탐색의 동작 과정 설명

3. 이진 탐색 알고리즘이 종료되는 조건 두가지

4. 이진 탐색 알고리즘 시간 복잡도

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