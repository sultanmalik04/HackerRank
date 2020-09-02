>collections.Counter()
A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.


## Python
```python
from collections import Counter

no_shoes = int(input())
shoes_sizes = Counter(list(map(int, input().split())))
no_customers = int(input())
total = 0
for i in range(no_customers):
    size, money = map(int, input().split())
    if shoes_sizes[size] > 0:
        shoes_sizes[size] -= 1
        total += money
print(total)
```