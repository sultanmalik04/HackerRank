### Problem Statement
> Using Bubble Sort algorithm, sort the array and find the number of swaps taken place.

## Python
```python
def countSwaps(a):
    c = 0
    n = len(a)
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j+1]:
                c += 1
                a[j], a[j+1] = a[j+1], a[j]
    print(f'Array is sorted in {c} swaps.')
    print('First Element:', a[0])
    print('Last Element:', a[-1])
```