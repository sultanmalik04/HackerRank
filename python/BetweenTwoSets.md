## Python
```python
def arrayIsFactorOfk(a, k):
    ret = True
    for i in a:
        if k%i != 0:
            ret = False
    return ret

def kIsFactorofArray(a,k):
    ret = True
    for i in a:
        if i%k != 0:
            ret = False
    return ret

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
count = 0
for i in range(max(a), min(b)+1):
    if arrayIsFactorOfk(a, i) and kIsFactorofArray(b, i):
        count += 1
print(count)
```