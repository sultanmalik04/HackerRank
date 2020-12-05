#### Problem Statement
>Given two strings, determine if they share a common substring. A substring may be as small as one character.

## Python
```python
from collections import defaultdict
# Complete the twoStrings function below.
def twoStrings(s1, s2):
    d = defaultdict(int)
    for i in s1:
        d[i] += 1
    for i in s2:
        if d[i] > 0:
            return "YES"
    return "NO"
q = int(input())

for q_itr in range(q):
    s1 = input()

    s2 = input()

    result = twoStrings(s1, s2)
    print("result")
```