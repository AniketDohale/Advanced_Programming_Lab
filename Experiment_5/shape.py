class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, n):
        return Point(self.x * n, self.y * n)

    def __imul__(self, n):
        self.x *= n
        self.y *= n
        return self

    def __truediv__(self, n):
        return Point(self.x / n, self.y / n)

    def __itruediv__(self, n):
        self.x /= n
        self.y /= n
        return self


x = int(input("Enter Value of x for p -> "))
y = int(input("Enter Value of y for p -> "))
p = Point(x, y)

x = int(input("Enter Value of x for q -> "))
y = int(input("Enter Value of y for q -> "))
q = Point(x, y)

x = int(input("Enter Value of x for r -> "))
y = int(input("Enter Value of y for r -> "))
r = Point(x, y)

n = int(input("Enter Value of n -> "))

print("-----------------------")
p = q + r
print("p = q + r :", p.x, p.y)

p += q
print("p += q :", p.x, p.y)

p = q - r
print("p = q - r :", p.x, p.y)

p -= q
print("p -= q :", p.x, p.y)

p = q * n
print("p = q * n :", p.x, p.y)

p *= n
print("p *= n :", p.x, p.y)

p = q / n
print("p = q / n :", p.x, p.y)

p /= n
print("p /= n", p.x, p.y)
print("-----------------------")
