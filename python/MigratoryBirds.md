### problem statement
>You have been asked to help study the population of birds migrating across the continent. Each type of bird you are interested in will be identified by an integer value. Each time a particular kind of bird is spotted, its id number will be added to your array of sightings. You would like to be able to find out which type of bird is most common given a list of sightings. Your task is to print the type number of that bird and if two or more types of birds are equally common, choose the type with the smallest ID number.


## python
```python
from collections import defaultdict

def migratoryBirds(arr):
    d = defaultdict(int)
    for i in arr:
        d[i] += 1
    result, maxval = 0, 0
    for i in sorted(d):
        if d[i] > maxval:
            maxval = d[i]
            result = i
    return result
```