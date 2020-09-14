#### Height Of a binary tree

## Python
```python
def height(root):
    if root == None:
        return -1
    else:
        lheight = 1 + height(root.left)
        rheight = 1 + height(root.right)

        if lheight > rheight:
            return lheight
        else:
            return rheight
```