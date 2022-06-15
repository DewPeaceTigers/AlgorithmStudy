## 정민

1. 이진탐색의 조건은?
    - 탐색할 배열이 오름차순 정렬되어있는 상태여야 한다.

2. 순차탐색과 이진탐색의 시간복잡도는?
    - 순차탐색: O(N)
    - 이진탐색: O(logN)
    - n의 숫자가 크면 클수록 선형탐색보다 이진 탐색으로 탐색하는 것이 훨씬 효율적임
    
3. 이진탐색의 동작과정을 설명해주세요.
    1. 배열의 중간값을 가져온다.
    2. 중간값과 찾는 값의 데이터를 비교한다.
        - 중간값 == 찾는값 : 종료!
        - 중간값 < 찾는값 : 중간값 기준 배열의 오른쪽 구간을 탐색한다.
        - 중간값 > 찾는값 : 중간값 기준 배열의 왼쪽 구간을 탐색한다.
    3. 값을 찾거나 간격이 비어있을 때까지 반복합니다.
    
4. 재귀함수를 이용하여 이진탐색을 구현한 코드입니다. 빈칸을 채워주세요!
    
    ```python
    def binary_search(array, target, start, end) :
      # 종료조건
      if start > end :
        return None

      mid = (start+end)//2
    
      if target == array[mid] :
        return mid
 
      elif target < array[mid] :
        return binary_search(array, target, start, mid-1)

      else :
        return binary_search(array, target, mid+1, end)
    ```
    
5. 이진 탐색을 쉽게 구현할 수 있도록 파이썬에서 제공하는 라이브러리는?  
그리고 해당 라이브러리에서 가장 많이 사용되는 메소드(2가지)는?
  - bisect 라이브러리
  - 대표 메소드
      - bisect_left() : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메소드
      - bisect_right() : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메소드