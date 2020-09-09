#### Problem Statement
>Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.

## Python

```python
s = sorted(input())   # sort the input string for alphabetical ordering
dic = defaultdict(int)
for i in s:
    dic[i] += 1
result = sorted(dic.items(), key=lambda kv: kv[1], reverse=True) # sort dict based on the value
for i in range(3):
    print(*result[i])
```