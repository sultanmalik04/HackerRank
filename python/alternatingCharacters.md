### Problem Statement
> You are given a string containing characters A  and B only. Your task is to change it into a string such that there are no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.  
Your task is to find the minimum number of required deletions.

## Python
```python
def alternatingCharacters(s):
    c = 0 # for counting deletion
    prev = s[0]
    temp = s
    for i in temp[1:]:
        if i == prev:
            c += 1    
        else:
            prev = i
    return c
```