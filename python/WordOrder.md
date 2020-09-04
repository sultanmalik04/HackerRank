## Python
```python
from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    s = input()
    if s in d:
        d[s] += 1
    else:
        d[s] = 1
print(len(d))
for key, value in d.items():
    print(value, end=" ")
```