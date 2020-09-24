#### Problem Statement
> Rotate a given array 'a' in left direction by d position.

## Python
```python
def rotLeft(a, d):
    ret = []
    n = len(a)
    for i in range(d, n):
        ret.append(a[i])
    for j in range(0, d):
        ret.append(a[j])
    return ret
```