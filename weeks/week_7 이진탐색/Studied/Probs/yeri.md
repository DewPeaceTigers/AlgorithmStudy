## 예리

1. 이진탐색은 \_\_\_된 자료구조를 바탕으로 한다.

2. 이진 탐색은 반복 구조로 구현할 수 있다. 아래 빈칸에 들어갈 코드를 작성하세용

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

3. 이진 탐색의 시간 복잡도는?

4. 이진 탐색은 **\_** 알고리즘을 응용한 것이다.

5. 파이썬에서 이진탐색을 위해 사용할 수 있는 라이브러리는?
