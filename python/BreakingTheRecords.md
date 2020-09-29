## Python
```python
n = int(input())
scores = list(map(int, input().split()))
minMax = [scores[0], scores[0]]
result = [0, 0]

for i in scores:
    if i > minMax[0]:
        minMax[0] = i
        result[0] += 1
    if i < minMax[1]:
        minMax[1] = i
        result[1] += 1
print(*result)
```