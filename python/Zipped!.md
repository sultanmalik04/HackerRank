#### Problem statement
>Use of zip(*iterable)      
This function returns a list of tuples. The ith tuple contains the ith element from each of the argument sequences or iterables.          
If the argument sequences are of unequal lengths, then the returned list is truncated to the length of the shortest argument sequence.


## Python
```python
N, X = map(int, input().split())
subject_marks = []
for _ in range(X):
    marks = list(map(float, input().split()))
    subject_marks.append(marks)
for i in list(zip(*subject_marks)):
    print(sum(i)/X)
```