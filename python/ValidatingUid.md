#### Problem Statement
> A valid Uid follows following rules:          
1- It must contain at least 2 uppercase English alphabet characters.      
2- It must contain at least 3 digits (0 - 9).      
3- It should only contain alphanumeric characters (a-z , A-Z & 0-9).    
4- No character should repeat.       
5- There must be exactly 10 characters in a valid UID.


## Python
```python
for _ in range(int(input())):
    uid = input()
    uppercase = 0
    digits = 0
    if len(uid) == 10 and len(uid) == len(set(uid)) and uid.isalnum():
        for i in uid:
            if i.isdigit():
                digits += 1
            if i.isupper():
                uppercase += 1
        if digits >= 3 and uppercase >= 2:
            print('Valid')
        else:
            print('Invalid')
    else:
        print('Invalid')
```