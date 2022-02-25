# 이진탐색

- 정렬된 배열에서 타겟을 찾는 검색 알고리즘
- 자료구조인 이진 탐색 트리와 알고리즘 그 자체이다.
- 탐색할 자료를 둘로 나누어 해당 데이터가 있을 만한 곳을 탐색하는 방법
- 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 특징
- 위치를 나타내는 변수 3개를 사용
  : 탐색하고자 하는 범위의 시작점, 끝점, 중간점

## 동작

1. 배열의 중간 값을 가져온다.
2. 중간 값과 검색 값을 비교
   - 중간 값이 검색 값과 같다면 종료. (mid = key)
   - 중간 값보다 검색 값이 크다면 중간값 기준 배열의 오른쪽 구간을 대상으로 탐색(mid < key)
   - 중간 값보다 검색 값이 작다면 중간값 기준 배열의 왼쪽 구간을 대상으로 탐색 (mid > key)
3. 값을 찾거나 간격이 비어있을 때까지 반복

> ❌종료 조건❌
>
> - 검색을 성공한 경우 : 리스트에서 검색할 값을 찾았을 때 종료된다
> - 검색을 실패한 경우 : 더 이상 검색할 범위가 없을 경우 종료된다

## 구조

**분할 정복 알고리즘**을 이용함

- Divide ande Conquer
  - Divide : 문제를 하나 또는 둘 이상으로 나눈다.
  - Conquer : 나눠진 문제가 충분히 작고 해결이 가능하다면 해결하고 그렇지 않으면 다시 나누기

➡️ 이진 탐색

- Divide : 리스트를 두 개의 서브 리스트로 나눔
- Conquer
  - 검색할 숫자 > 중간 값 : 뒷 부분의 서브 리스트에서 숫자 찾기
  - 검색할 숫자 < 중간 값 : 앞 부분의 서브 리스트에서 숫자 찾기

## 구현

1. 재귀

```python
def binary_search(left,right):
	if left<= right:
    	mid = (left+right)//2

        if nums[mid]<target:
        	return binary_search(mid+1,right)
       	elif nums[mid]>target:
        	return binary_search(left,mid-1)
        else:
        	return mid
    else:
    	return -1
```

2. 반복

```python
def binary_search():
	left,right=0,len(nums)-1
    while left<=right:
    	mid=(left+right)//2

        if nums[mid]<target:
        	left=mid+1
        elif nums[mid]>target:
        	right=mid-1
        else:
        	return mid
    return -1
```

3. 모듈 bisect 사용하기

```python
def binary_search():
	index=bisect.bisect_left(nums,target)

    if index<len(nums) and nums[index]==target:
    	return index
    else:
    	return -1
```

> - bisect_left(a, x) --> 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메소드
> - bisect_right(a, x) --> 정렬된 순서를 유지하도록 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메소드

➡️ bisect라이브러리(모듈)은 '정렬된 리스트'에서 '값이 특정 범위에 속하는 원소의 개수'를 구할 때 사용하면 효율적이다.

```python
# 효율적 예시
from bisect import bisect_left, bisect_right

# '정렬된 리스트'에서 `값이 특정 범위에 속하는 원소의 개수`를 구할 때 좋다.
def count_by_range(b, left_value, right_value):
    right_index = bisect_right(b, right_value)
    left_index = bisect_left(b, left_value)
    print('right : ', right_index, 'left :', left_index)
    return right_index - left_index


a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(a, 4, 4))
>>> right :  8 left : 6
>>> 2
# 리스트 a에 4는 총 2개 존재한다.

print(count_by_range(a, -1, 3))
>>> right :  6 left : 0
>>> 6
# 리스트 a에 -1~3사이의 값은 총 6개 존재한다.
```

## 시간복잡도

n개의 리스트를 매번 2로 나누어 1이 될 때까지 비교연산을 k회 진행

> n = 2^k = log2n = log22^k <br/>
> log2n = k <br/>
> k+1이 최종 시간 복잡도 (1일때도 비교연산 수행) <br/>
> O(logn)

## 💛 Tip

> 💡 코딩테스트의 이진탐색 문제는 탐색 범위가 큰 상황에서의 탐색을 가정하는 문제가 많다.
>
> 탐색 범위가 2,000만을 넘어가면<br/>
> 처리해야 할 데이터의 개수나 값이 1,000만 단위 이상<br/>
> ➜ 이진 탐색으로 문제에 접근해보기!<br/>

[참고]

- https://velog.io/@kimdukbae/%EC%9D%B4%EB%B6%84-%ED%83%90%EC%83%89-%EC%9D%B4%EC%A7%84-%ED%83%90%EC%83%89-Binary-Search
- 파이썬 알고리즘 인터뷰(도서)
