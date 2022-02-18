## 정민
1. 이미 데이터가 정렬되어 있는 경우 빠르게 동작하는 정렬 알고리즘
- 삽입 정렬 → 시간복잡도 : O(N)

2. 퀵 정렬에서 평균/최악의 시간 복잡도와 어떠한 경우가 최악이 되는지
- 최선 : O(NlogN)
- 최악 : O(N^2) → 정렬하고자 하는 배열이 오름차순 정렬 되어있거나 내림차순 정렬 되어있는 경우

3. 아래 퀵정렬 소스코드에서 빈칸을 채우세요. (퀵 정렬이 끝나는 조건)
    ```python
    def quick_sort(arr):
        # 재귀 함수 종료 조건
        if len(arr)<=1
            return arr
        
        pivot = arr[0]
        tail = arr[1:] 
        
        left_side = [x for x in tail if x<=pivot]
        right_side = [x for x in tail if x>pivot] 
        
        return quick_sort(left_side) + [pivot] + quick_sort(right_side)
    ```

4. 분할 정복(Divide and Conquer) 방식을 사용한 정렬 알고리즘 2가지
- 퀵 정렬(Quick Sort), 합병 정렬(Merge Sort) 

5. 삽입 정렬의 수행 과정을 설명하세요.
    1) 현재 타겟이 되는 숫자와 이전 위치에 있는 원소들을 비교한다. (첫 번째 타겟은 두 번째 원소부터 시작한다.)
    2) 타겟이 되는 숫자가 이전 위치에 있던 원소보다 작다면 위치를 서로 교환한다.
    3) 그 다음 타겟을 찾아 위와 같은 방법으로 반복한다.