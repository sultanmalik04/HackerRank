#### Problem Statement
>Given 2 pointers to the head nodes of  linked lists that merge together at some point, find the node where the two lists merge. The merge point is where both lists point to the same node, i.e. they reference the same memory location. It is guaranteed that the two head nodes will be different, and neither will be NULL. If the lists share a common node, return that node's DATA value.

## Python
```python
def length(head):
    l = 0
    while head:
        l += 1
        head = head.next
    return l

def findMergeNode(head1, head2):
    l1 = length(head1)
    l2 = length(head2)
    if l1 > l2:
        for i in range(l1 - l2):
            head1 = head1.next
    else:
        for i in range(l2 - l1):
            head2 = head2.next
    while head1 and head2:
        if head1 == head2:
            return head1.data
        head1, head2 = head1.next, head2.next
```