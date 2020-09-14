### Tree Traversal

## Python
```python
# Preorder Traversal
def preOrder(root):
    if not root:
        return

    print(root.info,end=" ")
    preOrder(root.left)
    preOrder(root.right)

# Postorder Traversal
def postOrder(root):
    if not root:
        return

    postOrder(root.left)
    postOrder(root.right)
    print(root.info,end=" ")

# Inorder Traversal
def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print(root.info,end=" ")
    inOrder(root.right)