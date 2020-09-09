#### Problem Statement
>compare two linked list if they have same number of elements and there value is same 
then return 1 else return 0

## Python
```python
def compare_lists(llist1, llist2):
    if not llist1 and not llist2:
        return 1
    while llist1 and llist2:
        if llist1.data - llist2.data != 0:
            return 0
        llist1, llist2 = llist1.next, llist2.next
    if llist1 or llist2:
        return 0
    else:
        return 1
```