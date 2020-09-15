## Use Of Collections.namedtuple()
>Basically, namedtuples are easy to create, lightweight object types.
They turn tuples into convenient containers for simple tasks.
With namedtuples, you don’t have to use integer indices for accessing members of a tuple.

#### e.g.
```python
>>> from collections import namedtuple
>>> Point = namedtuple('Point','x,y')
>>> pt1 = Point(1,2)
>>> pt2 = Point(3,4)
>>> dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
>>> print dot_product
11
```
## Problem Statement
>you have given spreadsheet of students containing ID, MARKS, NAME, CLASS and you have to calculate the average marks of the students

NOTE: In input the columns will be given randomly (not in any order)

## Python
```python
from collections import namedtuple

N = int(input())
columns = input().split()
Students = namedtuple('Students', 'ID MARKS NAME CLASS')
marks_sum = 0
for _ in range(N):
    dic = {}
    dic[columns[0]], dic[columns[1]], dic[columns[2]], dic[columns[3]] = input().split()
    std = Students(ID = dic['ID'], MARKS = dic['MARKS'], NAME = dic['NAME'], CLASS = dic['CLASS'])
    marks_sum += int(std.MARKS)
print(marks_sum/N)
```