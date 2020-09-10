#### Problem Statement
>Given a reference to the head of a doubly-linked list and an integer,DATA , create a new DoublyLinkedListNode object having data value DATA  and insert it at the proper location to maintain the sort.

## Python
```python
def sortedInsert(head, data):
    newNode = DoublyLinkedListNode(data)
    if not head:
        head = newNode
        return head
    temp = head
    if temp.data >= data and not temp.prev:
        newNode.next = temp
        temp.prev = newNode
        head = newNode
    while temp:
        if temp.next == None and temp.data <= data:
            temp.next = newNode
            break
        if temp.data > data:
            newNode.next = temp
            temp.prev.next = newNode
            newNode.next = temp
            break
        temp = temp.next
    return head
```