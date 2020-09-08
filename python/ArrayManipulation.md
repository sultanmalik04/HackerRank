### Problem Statement
>Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in your array.

## Python
```python
def arrayManipulation(n, queries):
    result = [0]*(n+1)
    for i in queries:
        result[i[0]-1] += i[2]
        result[i[1]] -= i[2]
    s = 0
    max_sum = 0
    for i in range(n+1):
        s += result[i]
        max_sum = max(max_sum, s)   
    return max_sum
```