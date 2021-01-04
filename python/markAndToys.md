### Problem statement

> Given a list of toy prices and an amount to spend, determine the maximum number of gifts he can buy.

## Python
```python
def maximumToys(prices, k):
    No_of_gifts = 0
    prices.sort()
    i = 0
    while prices[i] < k and k > 0:
        k -= prices[i]
        i += 1
        No_of_gifts += 1
    return No_of_gifts
```
