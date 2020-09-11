#### Problem Statement
>Check whether brackes are balanced or not...

## Python
```python
def isBalanced(s):
    stack = []
    dic = {']':'[', ')':'(', '}':'{'}
    for i in s:
        if i in ['[', '(', '{']:
            stack.append(i)
        elif i in [']', ')', '}']:
            if len(stack) == 0:
                return 'NO'               
            openning = stack.pop()
            if openning != dic[i]:
                return 'NO'
    if len(stack) != 0:
        return 'NO'
    else:
        return 'YES'
```