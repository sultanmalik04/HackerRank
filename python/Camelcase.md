### Problem Statement
>CamelCase String having the following properties:       
It is a concatenation of one or more words consisting of English letters.     
All letters in the first word are lowercase.     
For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.

## Python
```python
def camelcase(s):
    ret = 1
    for i in s:
        if i.isupper():
            ret += 1
    return ret

s = input()
print(camelcase(s))
```