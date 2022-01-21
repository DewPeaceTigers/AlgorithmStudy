```python
def solution(n, lost, reserve):
    print(lost,set(lost))
    new_lost = set(lost) - set(reserve)
    print(new_lost)
    new_reserve = set(reserve) - set(lost)
    for i in new_lost:
        if i - 1 in new_reserve:
            new_reserve-={i - 1}
        elif i + 1 in new_reserve:
            new_reserve-={i+1}
        else:
            n-=1
    return n
```
