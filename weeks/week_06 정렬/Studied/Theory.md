# 정렬
원소들을 번호 순이나 사전 순서와 같이 일정한 순서대로 열거하는 알고리즘이다.  
다른 알고리즘을 최적화하는데 중요하게 이용됨.  
정규화나 의미있는 결과물을 생성하는 데 유용됨.  
정렬 알고리즘으로 데이터를 정렬하면 이진탐색(Binary Search)가 가능하다.

## 정렬 결과 조건
1. 출력은 비 내림차순이다.
2. 출력은 입력을 재배열하여 만든 순열이다.

## 선택 정렬(Select Sort)
선택 정렬은 현재 위치에 들어갈 값을 찾아 정렬하는 배열이다. 최소 선택 정렬은 오름차순으로 정렬이 되고, 최대 선택 정렬은 내림차순으로 정렬된다. 

### 과정
1. 정렬되지 않은 인덱스의 맨 앞에서부터, 배열 값 중 가장 작은 값을 찾아간다. 
2. 가장 작은 값을 찾으면, 그 값을 현재 인덱스의 값과 바꾸어준다. 
3. 다음 인덱스에서 위 과정을 반복해준다. 
![](https://images.velog.io/images/min-ji99/post/3de92cdf-e652-4c36-9ca5-cf833f4444e2/image.png)

### 시간 복잡도
이 알고리즘은 n-1개, n-2개, ... 2개, 1개 비교를 반복하므로 **시간복잡도는 O(N^2)**이다.
> **공간복잡도**
> 단 하나의 배열을 이용하기 때문에 O(N)이다.

### 장/단점
- 장점
  - 구현이 쉽다
  - 버블 정렬과 비교했을 때, 동일한 시간 복잡도를 갖지만 실제 시간을 측정해보면 버블 정렬에 보다 조금 더 빠른 정렬 방식이다
- 단점
  - 시간 복잡도가 O(N^2)이기 때문에 시간이 오래걸리는 정렬 방식이다


### 구현
```python
from random import randint
def selectionSort(arr):
    n=len(arr)
    for i in range(n-1):
        min_index=i
        for j in range(i+1, n) :
            if arr[j]<arr[i] :
                min_index=j
        arr[i], arr[min_index]=arr[min_index], arr[i]
    return arr

arr=[randint(1, 101) for i in range(5)]
print(selectionSort(arr))
```
## 삽입 정렬(Insert Sort)
현재 위치에서 배열들을 비교하여 들어갈 위치를 찾아, 그 위치에 삽입하는 배열 알고리즘이다.

### 과정
1. 삽입 정렬은 두번째 인덱스부터 시작한다. 
2. 현재 인덱스보다 왼쪽에 있는 원소들과 비교를 반복한다.
3. 만약 현재 인덱스 값이 비교하는 인덱스 값보다 크면 그 뒤에 삽입 변수를 저장한다.
![](https://images.velog.io/images/min-ji99/post/85937592-1e94-4b59-9184-4d3194ac8e59/image.png)
### 시간 복잡도
최악의 경우 n-1개, n-2개, ... 1개씩 비교를 반복하기 때문에 **시간복잡도는 O(N^2**)이다. 
> **공간 복잡도**
> 단 하나의 배열을 이용하기 때문에 O(N)이다.

### 장/단점
- 장점
  - 이미 정렬되어 있는 경우나 자료의 수가 적은 정렬에 매우 효율적이다.
  - 자료의 수가 적을 경우 구현이 간단하다
- 단점
  - 비교적 많은 원소들이 이동해야 한다
  - 자료의 수가 많고 자료의 크기가 클 경우 적합하지 않다

### 구현
```python
from random import randint

def insertSort(arr) :
    n=len(arr)
    for i in range(n) :
        for j in range(i, 0, -1) :
            if arr[j-1]>arr[j] :
                arr[j], arr[j-1]=arr[j-1], arr[j]
    return arr
arr=[randint(1, 101) for i in range(5)]
print(insertSort(arr))
```
## 버블 정렬(Bubble Sort)
인접한 두개 원소를 비교하여, 정한 기준의 값을 뒤로 넘겨 정렬하는 방법이다. 즉, 오름차순으로 정렬하고자 할 경우 비교할 때마다 더 큰 값이 뒤로 이동시킨다. 1바퀴 돌때마다 가장 큰 값이 맨 뒤에 저장된다. 맨 마지막에는 비교하는 수들 중 가장 큰 값이 저장 되기 때문에, (전체 배열의 크기)-(현재까지 순환한 바퀴 수)만큼 반복해주면 된다.

### 과정
1. 두 번째 인덱스부터 시작해서 현재 인덱스 값과 바로 이전의 인덱스 값을 비교한다.
2. 이전 인덱스 값이 더 크면 현재 인덱스와 바꾸어준다. 그렇지 않다면 다음 인덱스로 넘어가 배열 값을 비교한다.
3. 이를 (전체 배열의 크기)-(현재까지 순환한 바퀴 수)만큼 반복한다.
![](https://images.velog.io/images/min-ji99/post/b33daac9-4129-452d-bfdd-24bcda1109d5/image.png)
### 시간복잡도
버블 정렬 알고리즘은 n-1개, n-2개, ..., 1개씩 비교를 반복하므로 **시간 복잡도는 O(N^2)**이다.
> **공간복잡도**
> 단 하나의 배열에서만 진행하므로 O(N)이다.

### 장/단점
- 장점 
  - 인접한 값만 계속해서 비교하기 때문에 구현이 쉽다
  - 코드가 직관적이다
- 단점
  - 시간 복잡도가 O(N^2)이기 때문에 비효율적이다
### 구현
```python
from random import randint

def bubbleSort(arr) :
    for i in range(len(arr)-1, 0, -1) :
        for j in range(i) :
            if arr[j]>arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
arr=[randint(1, 101) for i in range(5)]
print(bubbleSort(arr))
```
## 퀵 정렬
분할 정복을 이용하여 정렬을 수행하는 알고리즘이다. Pivot point(기준이 되는 값)을 하나 정하고 이 값을 기준으로 작은 값은 왼쪽, 큰 값은 오른쪽으로 옮기는 방식으로 정렬한다. 이를 반복하여 분할된 배열의 크기가 1이 되면 모두 정렬된 것이다.
>분할(Divide) : 입력 배열을 pivot 기준으로 비균등하게 2개의 부분 배열로 분할한다  
>정복(Conquer): 부분 배열을 정렬한다. 부분 배열의 크기가 충분히 작지 않으면 순환 호출을 이용하여 다시 분할 정복 방법을 적용한다.  
>결합(Combine): 정렬된 부분 배열들을 하나의 배열에 합병한다.

병합 정렬과 차이점은 병합은 분할 단계에서 아무것도 하지 않고 병합시 정렬하지만, 퀵은 분할 단계에서 정렬하고, 병합시 아무것도 하지 않는다.

### 과정
1. pivot point를 하나 정한다. 보통 맨 앞, 맨 뒤, 중간값이나 랜덤값으로 정한다.
2. pivot을 기준으로 작은 원소들은 pivot의 왼쪽으로, 큰 원소들은 pivot의 오른쪽으로 옮긴다.
3. pivot을 제외한 왼쪽 리스트와 오른쪽 리스트를 다시 정렬한다.
  분할된 부분 리스트에 대하여 순환 호출을 이용하여 정렬을 반복한다.
  부분 리스트에서도 다시 pivot을 정하고 pivot을 기준으로 2개의 부분 리스트로 나누는 과정을 반복한다.
4. 부분 리스트들이 더 이상 분할이 불가능할 때까지 반복한다.(리스트의 크기가 0이나 1이 될때까지 반복)
![](https://images.velog.io/images/min-ji99/post/76f7449b-49d7-4a66-a101-9082ca2680a1/image.png)
### 시간복잡도
pivot의 따라 **최선의 경우에는 O(NlogN), 최악의 경우에는 O(N^2)**을 갖는다.
### 장/단점
- 장점
  - 시간복잡도가 O(NlogN)이기 때문에 실행시간이 준수한 편이다
- 단점
  - 기준값(Pivot)에 따라서 시간 복잡도가 크게 달라진다. 최악의 Pivot을 선택할 경우 O(N^2)이라는 시간 복잡도를 갖게 된다
- 퀵 정렬은 이미 데이터가 정렬되어 있는 경우에는 매우 느리게 동작한다!
### 구현
```python
from random import randint

arr=[randint(1, 101) for i in range(5)]

def quickSort(arr, start, end):
    if start >= end :
        return
    pivot=start
    left, right=start+1, end

    while left<=right:
        while left<=end and arr[left] <=arr[pivot] :
            left+=1
        while right>start and arr[right]>=arr[pivot] :
            right-=1
        if left>right:
            arr[right], arr[pivot]=arr[pivot], arr[right]
        else:
            arr[right], arr[left]=arr[left], arr[right]
    quickSort(arr, start, right-1)
    quickSort(arr, right+1, end)

quickSort(arr, 0, len(arr)-1)
print(arr)
```
## 합병 정렬(Merge Sort)
합병 정렬은 분할 정복방식으로 설계된 알고리즘이다. 분할 정복은 큰 문제를 반으로 쪼개 문제를 해결해 나가는 방식으로, 배열의 크기가 1보다 작거나 같을 때까지 반복한다.
입력으로 하나의 배열을 받고, 두 개의 배열로 계속 쪼게 나간 후, 합치면서 정렬을 해 하나의 정렬을 출력한다.
합병을 할 때는 두 개의 배열을 비교하여, 기준에 맞는 값을 다른 배열에 저장해 나간다. 

➡️ 재귀함수로 구현하게 됨

> 분할(Divide): 입력 배열을 같은 크기의 2개의 부분 배열로 분할한다.  
> 정복(Conquer) : 부분 배열을 정렬한다. 부분 배열의 크기가 충분히 작지 않으면 순환 호출을 이용하여 다시 분할 정복 방법을 적용한다.  
> 결합(Combine): 정렬된 부분 배열들을 하나의 배열에 합병한다.

### 과정
- 분할 과정
  1. 배열의 시작 위치와 종료 위치 둘을 더한 후 2를 나눠 그 위치를 기준으로 반으로 나눈다.
  2. 분할한 배열의 크기가 0 또는 1 일때까지 반복한다.
  
- 합병 과정
  1. 두 배열 A, B의 각각의 인덱스(i, j)를 저장한다.
  2. A[i]와 B[j]를 비교하여 이 중에 작은 값을 새 배열에 저장한다.
    새 배열에 저장한 원소가 있는 배열의 인덱스를 1 증가 시킨다.
  3. 두 배열 중 하나의 배열이 끝에 도달할 때까지 반복하고 끝까지 못 간 배열은 순서대로 저장시킨다.
![](https://images.velog.io/images/min-ji99/post/4fe13201-0d05-4f62-a29a-b9c28bf1d0ea/image.png)

### 시간 복잡도
크기가 N인 배열을 한번 분할할 때 2개, 4개, 8개 ... 반복하므로 logN만큼 반복하고 각 분할 별로 합병을 진행하므로 시간 복잡도는 O(NlogN)이다.
>공간복잡도  
>정렬을 위한 배열을 하나 더 생성하므로 2N개 사용한다.

### 장/단점
- 장점
  - 원본 배열을 반으로 분할해가면서 정렬하기 때문에 시간복잡도가 O(NlogN)으로 준수하다
  - 퀵 정렬과 달리, Pivot을 설정하는 과정 없이 무조건 절반으로 분할하기 때문에 Pivot에 따라 성능이 좌우되지 않는다.
- 단점
  - 추가적인 메모리가 필요하다.

### 구현
```python
from random import randint

arr=[randint(1, 101) for i in range(5)]

def mergeSort(arr):
    if len(arr) < 2:
        return arr
    mid=len(arr)//2
    left_arr=mergeSort(arr[:mid])
    right_arr=mergeSort(arr[mid:])

    merged_arr=[]
    l=h=0
    while l < len(left_arr) and h<len(right_arr) :
        if left_arr[l]<right_arr[h] :
            merged_arr.append(left_arr[l])
            l+=1
        else:
            merged_arr.append(right_arr[h])
            h+=1
    merged_arr+=left_arr[l:]
    merged_arr+=right_arr[h:]
    return merged_arr
print(mergeSort(arr))
```
[출처]
이미지 - https://gmlwjd9405.github.io/2018/05/06/algorithm-selection-sort.html