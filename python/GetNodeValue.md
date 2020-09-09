#### Problem Statement
>You’re given the pointer to the head node of a linked list and a specific position. Counting backwards from the tail node of the linked list, get the value of the node at the given position. A position of 0 corresponds to the tail, 1 corresponds to the node before the tail and so on.

## Python
```python
def getNode(head, positionFromTail):
    temp = head
    l = 0
    while temp:
        l += 1
        temp = temp.next
    print(head.data)
    position = l - positionFromTail - 1
    while position:
        head = head.next
        position -= 1
    return head.data
```