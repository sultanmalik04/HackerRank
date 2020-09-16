## Python
```python
def topView(root) : 
  
    if(root == None) : 
        return
    q = [] 
    dic = dict() 
    hd = 0
    root.hd = hd  
    q.append(root)  
  
    while(len(q)) : 
        n = q[0] 
        hd = n.hd   
        if hd not in dic: 
            dic[hd] = n.info  
        if(n.left) :          
            n.left.hd = hd - 1
            q.append(n.left)  
          
        if(n.right):          
            n.right.hd = hd + 1
            q.append(n.right)  
          
        q.pop(0) 
    for i in sorted (dic): 
        print(dic[i], end = " ") 
```