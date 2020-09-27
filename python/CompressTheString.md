### Problem Statement
>You are given a string S . Suppose a character 'c' occurs consecutively X times in the string. Replace these consecutive occurrences of the character 'c' with (X, c) in the string.


## python
```python
from itertools import groupby

s = input()

print(*[(len(list(i)), int(k)) for k,i in groupby(s)])
```