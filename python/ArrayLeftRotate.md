#### Problem Statement
> Rotate a given array 'a' in left direction by d position.

## Python
```python
def rotLeft(a, d):
    n = len(a)
    return a[d:n] + a[0:d]
```