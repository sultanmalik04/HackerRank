>An "OrderedDict" is a dictionary subclass that remembers the order that keys were first inserted.

>The rpartition() method searches for the last occurrence of a specified string, and splits the string into a tuple containing three elements.

## Python
```python
from collections import OrderedDict
dictionary = OrderedDict()
for _ in range(int(input())):
    item_name, space, price = input().rpartition(" ")
    price = int(price)
    if item_name in dictionary:
        dictionary[item_name] += price
    else:
        dictionary[item_name] = price
for key, t_price in dictionary.items():
    print(key, t_price)
```