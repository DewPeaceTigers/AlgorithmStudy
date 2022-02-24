## 정민

1. 이진탐색의 조건은?

2. 순차탐색과 이진탐색의 시간복잡도는?
    
3. 이진탐색의 동작과정을 설명해주세요.
    
4. 재귀함수를 이용하여 이진탐색을 구현한 코드입니다. 빈칸을 채워주세요!
    
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
    
5. 이진 탐색을 쉽게 구현할 수 있도록 파이썬에서 제공하는 라이브러리는?  
그리고 해당 라이브러리에서 가장 많이 사용되는 메소드(2가지)는?
