#### Problem Statement
>You’re given the pointer to the head node of a doubly linked list.revese the order of node.

## Python
```python
def reverse(head):
    if not head:
        return head
    temp = head
    while temp:
        prev = temp.prev
        temp.prev = temp.next
        temp.next = prev
        head = temp
        temp = temp.prev
    return head
```