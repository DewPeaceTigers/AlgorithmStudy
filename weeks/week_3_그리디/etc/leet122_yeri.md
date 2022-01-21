[문제](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for i in range(len(prices)-1):
            print(i)
            if prices[i]<prices[i+1]:
                profit+=prices[i+1]-prices[i]
        return profit
```

⬇️

pythonic

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return(max(prices[i+1]-prices[i],0) for i in range(len(prices)-1))
```
