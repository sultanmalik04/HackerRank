#### Problem Statement
>There is a horizontal row of  cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if CUBEi is on top of CUBEj then sideLengthj >= sideLengthi.

```python
for _ in range(int(input())):
    n = int(input())
    cubeS = list(map(int, input().split()))
    pile = float('inf')
    result = 'Yes'
    while cubeS:
        num = cubeS.pop(0) if cubeS[0] > cubeS[-1] else cubeS.pop(-1)
        if num > pile: 
            result = 'No'
        pile = num
    print(result)
```