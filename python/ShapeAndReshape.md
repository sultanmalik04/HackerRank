#### Problem Statement
> numpy.shape:       
a)  Using shape to get the dimention of array.    
my__2D_array = numpy.array([[1, 2],[3, 4],[6,5]])
print my_2D_array.shape ........  #(3, 2) -> 3 rows and 2 columns       
b)  Using to change array dimentions.       
change_array = numpy.array([1,2,3,4,5,6]    
change_array.shape = (3, 2)         
print change_array 

> numpy.reshape():      
The reshape tool gives a new shape to an array without changing its data. It creates a new array and does not modify the original array itself.     
my_array = numpy.array([1,2,3,4,5,6])       
print numpy.reshape(my_array,(3,2))


## Python
```python
import numpy

arr = numpy.array(input().split(), int)
print(numpy.reshape(arr, (3,3)))
```