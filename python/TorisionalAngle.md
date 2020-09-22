#### Problem Statement
> Find the Torisional Angle in degrees

## Python
```python
import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        diff = []
        diff.append(self.x - no.x)
        diff.append(self.y - no.y)
        diff.append(self.z - no.z)
        obj = Points(*diff)
        return obj

    def dot(self, no):
        return self.x * no.x + self.y * no.y + self.z * no.z

    def cross(self, no):
        product = []
        product.append(self.y * no.z - self.z * no.y)
        product.append(self.z * no.x - self.x * no.z)
        product.append(self.x * no.y - self.y * no.x)
        obj = Points(*product)
        return obj

        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
```