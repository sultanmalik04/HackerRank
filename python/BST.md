## Python
```python
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def search(root,data):
    if root == None or root.data == data:
        return root
    
    if root.data < data:
        return search(root.right,data)
    else:
        return search(root.left,data)

def insert(root,node):
    if root == None:
        root = node
    else:
        if root.data < node.data:
            if root.right == None:
                root.right = node
            else:
                insert(root.right,node)
        else:
            if root.left == None:
                root.left = node
            else:
                insert(root.left,node)

def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print(root.data,end=" ")
    inOrder(root.right)

# function to find the inorder successor
# mean the mininmum value in the right subtree
def mnValueNode(node):
    current = node

    while current.left != None:
        current = current.left

    return current

# function to delete the specified data from the tree
def delete(root,data):
    if root is None: # if tree is empty
        return root

    # if the data to be deleted is graeter then the root's data then we have to 
    # go to right subtree else if data is data is less then the root's data then 
    # we hav eto go to the left subtree 
    if data > root.data:
        return delete(root.right,data)
    elif data < root.data:
        return delete(root.left,data)
    # if data to be deleted is equal to the root's data then that's the node we have to delete
    else:
        # if the targeted node has only one child
        if root.left is None:  
            temp = root.right
            root = None
            return temp
        
        elif root.right is None:
            temp = root.left
            root = None
            return temp
            

        # if the targeted node has two children then we have to find the inorder successor
        temp = miValueNode(root.right)

        root.data = temp.data # put the inorder successor data to the targeted node

        root.right = delete(root.right,temp.data) # delete the inorder successor 
    return root

def height(node):
    if node is None:
        return -1
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)

        #Use the larger one
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1
```