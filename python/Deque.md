### collections.deque()
>A deque is a double-ended queue. It can be used to add or remove elements from both ends.

## Python
```python
from collections import deque
d = deque()
for _ in range(int(input())):
    op = input().split()
    if op[0] == 'append':
        d.append(op[1])
    elif op[0] == 'appendleft':
        d.appendleft(op[1])
    elif op[0] == 'pop':
        d.pop()
    elif op[0] == 'popleft':
        d.popleft()
print(*[i for i in d])
```