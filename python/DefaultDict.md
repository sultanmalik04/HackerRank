>collections.defaultdict()
The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet. If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.


## Python
```python
from collections import defaultdict 
n, m = map(int, input().split())
d = defaultdict(list)
for i in range(n):
    d['A'].append(input())
for i in range(m):
    x = input()
    index_list = [i+1 for i in range(len(d['A'])) if d['A'][i] == x]
    if len(index_list) > 0:
        print(*index_list)
    else:
        print(-1)
```