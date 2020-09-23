#### Problem statement
> Use of any() and all() Functions:       
any():   This expression returns True if any element of the iterable is true.If the iterable is empty, it will return False.      
all():   This expression returns True if all of the elements of the iterable are true. If the iterable is empty, it will return True.     

## Python
```python
n = int(input())
arr = input().split()
if all([i.isdigit() for i in arr]):
    if any([i == i[::-1] for i in arr]):
        print(True)
    else:
        print(False)
else:
    print(False)
```