#### Problem Statement
>You're given the pointer to the head node of a sorted linked list, where the data in the nodes is in ascending order. Delete as few nodes as possible so that the list does not contain any value more than once.

## Python
```python
def removeDuplicates(head):
    if not head:
        return head
    temp = head
    duplicates = []
    while temp:
        if temp.data not in duplicates:
            duplicates.append(temp.data)
            prev = temp
            temp = temp.next
        else:
            prev.next = temp.next
            temp = temp.next
    return head
```