#### Problem Statement
>use numpy.concatenate()       
->Two or more arrays can be concatenated together using the concatenate function with a tuple of the arrays to be joined:     
->You are given two integer arrays of size NXP and MXP ( N&M  are rows, and P is the column). Your task is to concatenate the arrays along axis 0.     



## Python
```python
# with two array
import numpy

n, m, p = map(int, input().split())
arr1 = []
for _ in range(n):
    arr1.append(numpy.array(input().split(), int))
arr2 = []
for _ in range(m):
    arr2.append(numpy.array(input().split(), int))
print(numpy.concatenate((arr1, arr2), axis = 0))
```

```python
# same proble can be solved with single array
import numpy

n, m, p = map(int, input().split())
arr = numpy.array([], int)
for _ in range(n+m):
    arr = numpy.concatenate((arr,numpy.array(input().split(), int)))

print(numpy.reshape(arr, (m+n, p)))
```