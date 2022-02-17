## 정민
1. 이미 데이터가 정렬되어 있는 경우 빠르게 동작하는 정렬 알고리즘

2. 퀵 정렬에서 평균/최악의 시간 복잡도와 어떠한 경우가 최악이 되는지

3. 아래 퀵정렬 소스코드에서 빈칸을 채우세요. (퀵 정렬이 끝나는 조건)
    ```python
    def quick_sort(arr):
        # 재귀 함수 종료 조건
        __________________
        __________________
        
        pivot = arr[0]
        tail = arr[1:] 
        
        left_side = [x for x in tail if x<=pivot]
        right_side = [x for x in tail if x>pivot] 
        
        return quick_sort(left_side) + [pivot] + quick_sort(right_side)
    ```

4. 분할 정복(Divide and Conquer) 방식을 사용한 정렬 알고리즘 2가지

5. 삽입 정렬의 수행 과정을 설명하세요.