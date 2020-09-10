#### Probblem staement
>A linked list is said to contain a cycle if any node is visited more than once while traversing the list.

## Python
```python
def has_cycle(head):
    if not head:
        return 0
    while head:
        if head.data != 'v':
            head.data = 'v'
            head = head.next
        else:
            return 1
    return 0
```