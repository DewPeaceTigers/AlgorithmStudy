## 스택
- 제한적 접근 : 한쪽 끝에서만 자료 관리
- LIFO : 나중에 들어온 게 가장 먼저 나가는 데이터 구조
### 구조

- LIFO, FILO
- 대표적 활용 : CPU의 프로세스 구조 함수 동작 방식
- 추상 자료형 ADT

    - push : 맨 위 항목 삽입
    - pop : 맨 위 항목 삭제
    - top : 스택 맨 위를 표시
    - isEmpty : 비었는지 확인
    - isFull : 가득 차 있는지 확인
    - getSize : 갖고 있는 element 수 반환
- 주 기능
	
    - push : 데이터 넣기
	1. isFull?
    	1. true : 오류 발생 및 종료
        2. ++top
        	1. top 위치에 데이터 추가
	
    - pop : 꺼내기
    1. isEmpty?
    	1. true : 오류 발생 및 종료
        2. top이 가리키는 데이터 삭제
        	1. --top
            2. return 성공 / 삭제한 데이터 반환   
> ⚠ 주의사항 ⚠
> - push(x) 연산 시 : 오버플로(Overflow) 주의!
>- pop() 연산 시 : 언더플로(Underflow) 주의!



### 특징
- 장점
    - 속도가 빠르다
    - 구조가 단순해 구현 쉽다
- 단점
    - 저장 공간 낭비 : 미리 확보해야 함
    - 최대 개수 정해야 함
### 구현
- Array
    - 장점
    	- 접근 속도가 빠름
        - 구현 쉬움
    - 단점
    	- 변경이 용이하지 않음
        - 크기가 동적이 아님
    - 검색이 많을 때 사용
- Linked List 
	
    - 장점
    	- 변경 용이 : 메모리 주소만 변경하면 됨
        - 크기가 동적임
    - 단점
    	- 접근 어려움 : 연속된 공간이 아니기 때문에
        - 포인터를 위한 추가 메모리 공간 필요
     - 변경이 많을 때 사용
### 구현 (파이썬)
파이썬에서는 별도의 라이브러리를 사용할 필요 X

<span style="color:blue">기본 리스트</span>에서 append()와 pop() 메서드를 이용
- append(x) : 리스트의 가장 뒤쪽에 데이터를 삽입
- pop() : 리스트의 가장 뒤쪽에서 데이터를 꺼냄

``` python
stack = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력

stack.pop()
stack.pop()
stack.pop()
stack.pop()

# 언더플로(Underflow) 주의! 
# '언더플로': 자료구조에 데이터가 전혀 들어있지 않은 상태에서 삭제 연산 수행
if stack: # 스택에 데이터가 있는지 확인
  stack.pop() 
```
출력
```
[5, 2, 3, 1]
[1, 3, 2, 5]
```
### Time Complexity
![](https://images.velog.io/images/kinnyeri/post/5800b67b-5421-4d3f-bf25-fc35d1af363b/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-01-09%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2011.06.37.png)



## 큐
- 줄 서는 구조
- FIFO : 가장 먼저 넣은 데이터를 가장 먼저 꺼내기
- 선입선출 방식
- 큐에서는 입출력이 다른쪽에서 일어남
- 삽입 - 후단(rear), 삭제 - 전단(front)
### 구조
- FIFO, LILO
- 대표적 활용 : Multi Tasking을 위한 프로세스 스케줄링 방식 구현에 사용
- 추상 자료형 ADT
	
    - enqueue : rear에 항목 추가
    - dequeue : front 항목 제거
    - peek : front 반환
    - isFull : 가득 차있는지 확인
    - isEmpty : 비어있는지 확인
   
- 주 기능
	
    - enqueue : 데이터 rear에 넣기
	
        `list.append(data)`
	
    - dequeue : 꺼내기
    	1. `data = list[0]`
    	2. `del list[0]`
    	3. `return data`
### 특징
- 장점
    - 입력 데이터 순서 정하는데 최적화
- 특정 상태에 따라 우선순위 결정하기도 함 (:우선순위 큐)
- end----front 형태

### 구현
- Array
    - 장점
        - 구현 쉬움
    - 단점
    	- 변경이 용이하지 않음
       - 크기가 동적이 아님
    - 검색이 많을 때 사용
- Linked List 
	
    - 장점
    	- 변경 용이 : 메모리 주소만 변경하면 됨
       - 크기가 동적임
    - 단점
        - 포인터를 위한 추가 메모리 공간 필요
     - 변경이 많을 때 사용
### 종류
- 선형 큐 Linear Queue
	
    - 기본적인 큐 형태 (막대)
    - 단점
    	- enqueue,dequeue가 많은 경우 비어있어도 자료 삽입 불가 경우 있음
       - 자료 위치 변경 어려움..
- 환형 큐 Circular Queue
선형 큐의 단점 보완
  - 배열의 처음과 끝을 연결해 원형으로 구성
  - 빈 공간 없이 front,end를 옮기면 됨
### 구현 (파이썬)
<span style="color:blue">**collections** 모듈에서 제공하는 **deque** 자료구조</span> 활용

데이터를 넣고 빼는 속도가 list 자료형에 비해 효율적

	> list의 pop(0) 시간복잡도: O(N)
    > deque의 popleft() 시간복잡도: O(1)
- **append(x)** : deque의 맨 뒤(오른쪽)에 데이터를 삽입
- **popleft()** : deque의 맨 앞(왼쪽) 요소 삭제
- clear() : 모든 요소 제거
- reverse() : deque 의 요소 거꾸로 뒤집기
```python
from collections import deque

queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5) # 맨 뒤에 원소 추가
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() # 맨 앞 원소 제거
queue.append(1)
queue.append(4)
queue.popleft()

print(list(queue)) # 모든 원소 출력
queue.reverse() # 거꾸로 뒤집기
print(queue)

queue.popleft()
queue.popleft()
queue.popleft()
queue.popleft()

# 언더플로(Underflow) 주의! 
# '언더플로': 자료구조에 데이터가 전혀 들어있지 않은 상태에서 삭제 연산 수행
if queue: # 큐에 데이터가 있는지 확인
  queue.popleft() 
```
출력
```
[3, 7, 1, 4]
deque([4, 1, 7, 3])
```
### Time Complexity
![](https://images.velog.io/images/kinnyeri/post/9a51ea17-2e4a-4c66-bd99-5e8603f440ec/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-01-11%20%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB%2012.54.57.png)

## 우선순위 큐
- 들어간 순서에 상관없이 우선순위가 높은 데이터가 먼저 나오는 큐
- 데이터들이 우선순위를 가지고 있어 우선순위가 높은 데이터가 먼저 출력됨
### 구조
- 힙 이용
	
    - 완전 이진 트리
    - 모든 노드에 저장된 값인 우선순위는 자식 노드의 값보다 크거나 같다.
    - 루트 노드에 우선순위가 가장 높은 데이터를 위치시키는 자료구조가 된다.
    - 힙에서 노드를 뺄 때마다 우선 순위가 높은 데이터가 먼저 나옴

    > 최대 힙 (max heap)
    >
    >    - 부모 노드의 키 값이 자식 노드의 키 값보다 크거나 같은 완전 이진트리
    > 최소 힙 (min heap)
    >  - 부모 노드의 키 값이 자식 노드의 키 값보다 작거나 같은 완전 이진트리
    

- 추상 자료형 ADT
	
    - Insert : item 삽입
    - Remove : 가장 우선순위가 높은 요소 삭제 및 반환
    - Find : 우선순위 가장 높은 요소 반환
    - Empty : 공백 상태인지 확인
    - Full : 포화 상태인지 검사
    - Display : 모든 요소 출력
- 주기능
	
    - 데이터 저장
    	1. input이 들어옴. 우선순위 낮다고 가정하고 맨 끝에 저장 
        ➡️ 저장 보다는 부모 노드가 될 것과 비교만 하는 편이 좋음
        2. 부모 노드와 우선순위를 비교해서 자식이 크면 자리를 바꾸면서 최소 힙의 구조를 유지할 때까지 반복
        
     - 데이터 삭제
      1. 힙의 루트 노드 반환 : 가장 우선순위가 높은 데이터를 빼는 것이므로
      2. 루트 노드 삭제 이후 힙의 구조 그대로 유지하기 (=heapify 과정)
         1. 루트 노드 반환 후 마지막 노드를 루트 노드로 옮기기
         2. 자식 노드와 우선순위를 비교하여 자리를 바꾸면서 최소 힙의 구조를 유지할 때까지 반복
         ➡️ 새로운 요소가 자식 노드들 보다 값이 크면 더 이상 교환 필요 없다.
### 구현
- 힙
	
    - 삭제, 삽입 과정 모두 부모와 자식 간의 비교만 이루어진다. 
    - 삭제: O(logn), 삽입: O(logn)
    - 힙 구현은 배열로! : 직관적이고 다루기 용이함
- 배열이나 연결리스트로 구현하지 않는 이유?
우선순위를 매기면서 중간에 들어가야 하는 것이 생기면 삽입 과정이 복잡해진다. 최악의 경우 모든 인덱스를 탐색할 수도 있다. (삭제: O(1), 삽입: O(n))
### 구현 (파이썬)
우선순위 큐를 구현할 때는 내부적으로 최소 힙(min heap) 또는 최대 힙(max heap) 이용
<span style="color:blue">PriorityQueue</span> 혹은 <span style="color:blue">**heapq**</span> 활용
- 파이썬 라이브러리에서는 **기본적으로 최소 힙 구조**를 이용
  - 최대 힙 구현: 일부터 우선순위에 해당하는 값에 음수 부호(-)를 붙여서 원래의 값으로 돌리는 방식 사용
- PriorityQueue 보다는 일반적으로 heapq가 더 빠르게 동작
>💡 수행 시간이 제한된 상황에서는 heapq 사용을 권장

<br>

#### PriorityQueue
- put(x) : 우선순위 큐에 원소 추가
- get() : 우선순위 큐 원소 삭제 및 반환

```python
from queue import PriorityQueue

que = PriorityQueue() # 우선순위 큐의 디폴트 사이즈: 무한대
# que = PriorityQueue(maxsize=8) # 사이즈 지정

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
que.put(5) # 우선순위 큐에 원소 추가
que.put(2)
que.put(3)
que.put(7)
print(que.get()) # 우선순위 큐 원소 삭제 (기본: 최소힙)
que.put(1)
que.put(4)
print(que.get())
```
출력
```
2
1
```
<br>

#### heapq
- heapq.heappush(q, x) : 우선순위 큐에 원소 추가
- heapq.heappop(q) : 우선순위 큐 원소 삭제 및 반환

``` python
import heapq

q = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
heapq.heappush(q, 5) # 우선순위 큐에 원소 추가
heapq.heappush(q, 2)
heapq.heappush(q, 3)
heapq.heappush(q, 7)
print(heapq.heappop(q)) # 우선순위 큐 원소 삭제 (기본: 최소힙)
heapq.heappush(q, 1)
heapq.heappush(q, 4)
print(heapq.heappop(q))
```
출력
```
2
1
```
### Time Complexity
- 트리 높이 : log2n
- 삽입 : O(log2n)
➡️ 최악 : 새로운 요소가 부모와의 비교 과정에서 루트노드까지 올라갈 경우, 트리의 높이 만큼의 비교 및 이동 연산이 필요하다.
- 삭제 : O(log2n)
➡️ 최악 : 마지막 노드가 루트 노드로 올라오고 난 후 자식과 비교 과정에서 마지막 레벨까지 내려갈 경우, 트리의 높이 만큼의 시간이 필요

**참고**
스택
- https://yoongrammer.tistory.com/45
- https://cloudstudying.kr/lectures/141

큐
- https://yoongrammer.tistory.com/46
- https://cloudstudying.kr/lectures/142

우선순위 큐
- https://chanhuiseok.github.io/posts/ds-4/
- https://euncero.tistory.com/135