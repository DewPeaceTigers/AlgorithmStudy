[문제 링크](https://leetcode.com/problems/queue-reconstruction-by-height/)

```python
# people.sort(reverse=True)
# 그냥 역순 정렬하면 두번째 인덱스도 역순 정렬되니깐 문제 조건과 맞지 않음
people.sort(key = lambda x: (-x[0], x[1]))
result=[]
for p in people:
    result.insert(p[1],p)
print(result)
```
