## 정민

1. 그리디 알고리즘이란?
    - 지금 당장 최적인 답을 선택하는 과정을 반복하여 결과를 도출하는 알고리즘

2. 그리디 알고리즘 조건 (최적해)
    - **탐욕스런 선택 조건(greedy choice property)**: 앞의 선택이 이후의 선택에 영향을 주지 않음
    - **최적 부분 구조 조건(optimal substructure)** : 매 순간의 최적의 해가 문제 전체에 대한 최적 해여야 함   

3. 그리디 알고리즘의 장단점
    - 장: 계산 속도가 빠르다
    - 단: 항상 최적화 되지 않는다

4. 거스름돈 문제 풀이 방법?   
[문제] 500, 100, 50, 10원짜리 동전으로 N원을 줄 때, 동전의 최소 개수
    - 그리디 알고리즘 이용
    - '가장 큰 화폐 단위부터' 돈을 거슬러준다 (500 -> 100 -> 50 -> 10)
    - 동전의 단위가 서로 배수인 형태이기 때문에 그리디 알고리즘을 적용하여 풀 수 있음
    > 만약 화폐의 단위가 무작위(500, 400, 100원)일 경우 풀이 방법?
    - 다이나믹 프로그래밍 이용

5. 대표적인 그리디 알고리즘 종류는?
- 거스름돈 문제, 부분 배낭 문제, 크루스칼 알고리즘, 다익스트라 알고리즘

## 예리

1. 그리디란 여러 선택 중 하나를 고를 때, 매순간 \_\_ 이라고 생각되는 경우를 고르는 알고리즘이다.

   최적

2. 부분 배낭 문제가 그리디인 이유를 설명하시오.

   그 순간에 가장 가치가 큰 것을 넣기 때문이다. 무게/가치 를 기준으로 내림차순으로 정렬된 것에서 맨 앞부터 배낭에 넣는다.

3. 다이나믹 프로그래밍과의 차이점을 설명하세용

   다이나믹 프로그래밍은 하위 문제의 솔루션을 먼저 찾은 후 범위를 넓혀 전역에 대한 해결책을 찾지만, 그리디 알고리즘는 각 단계마다 로컬 최적해를 찾아 범위를 좁혀가 문제를 해결한다.

4. Kruskal Algorithm의 동작 방법을 간단히 설명하시오

   1. 그래프의 간선들을 가중치의 오름차순으로 정렬
   2. 정렬된 간선 리스트에서 순서대로 사이클을 형성하지 않는 간선 선택
      - 가장 낮은 가중치 먼저 선택
      - 사이클 형성하는 간선 제외
   3. 해당 간선을 현재 MST 집합에 추가


5. 그리디 알고리즘의 한계점은?

   최적임을 증명할 필요가 있다. 최적이지 못하면 근사치 추정일 뿐이다.
   
   최적의 조건

   - 최적 부분 구조 : 문제의 최적 해결 방법이 부분 문제에 대한 최적 해결 방법으로 구성되는 구조
   - 탐욕적 선택 속성 : 앞의 선택이 다른 선택에 영향을 주지 못한다.

 ## 민지

1. 탐욕법 알고리즘이란?

    현재 상황에서 최적인 답을 선택하여 적합한 결과를 도출하는 알고리즘이다. 그렇다고 현재 상황에서 최적의 선택이 최종적인 결과에 대한 최적해를 보장해주는 것이 아니기 때문에 탐욕법으로 문제가 해결되는지 파악 후 적용해야 한다.


2. 탐욕법 알고리즘의 조건

    선택으로 인해 전체 문제의 최적해를 반드시 도출할 수 있어야하며 문제에 대한 최종 해결 방법이 부분 문제에 대해서도 최적의 해결 방법이어야한다.

3. 지불해야하는 값이 n원일 때 1원, 50원, 100원, 500원 동전으로 동전의 개수를 최소로 지불하는 방법을 설명

    금액이 가장 큰 동전부터 최대한 지불할 수 있는 만큼 지불하는 방식으로 구현하면 된다. 4120원일 경우 500원 8개를 사용하고 남은 금액 120원의 경우 100원 1개 10원 2개를 지불하면 된다.

4. 탐욕 알고리즘의 한계

    반드시 최적의 해를 구할 수 있는 게 아니다.
  

5. 3번의 동전 문제에서의 한계(8원, 6원, 4원, 1원으로 할경우)

    10원을 만들경우 그리디 알고리즘을 사용하면 8 1 1 로 3개를 이용하지만 실제로는 6원과 4원을 사용하여 총 2개의 동전으로 지불할 수 있다.
