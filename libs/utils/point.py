class Point:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, multiplier):
        """For x * 2"""
        return Point(self.x * multiplier, self.y * multiplier)

    def __rmul__(self, multiplier):
        """For 2 * x"""
        return Point(self.x * multiplier, self.y * multiplier)

    def __floordiv__(self, dividor):
        """For the // operator, returns ints"""
        return Point(self.x // dividor, self.y // dividor)

    def __truediv__(self, dividor):
        """For the / operator, returns floats"""
        return Point(self.x / dividor, self.y / dividor)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def isInBound(self, bound):
        return self.x >= 0 and self.y >= 0 and self.x <= bound.x and self.y <= bound.y

    def isInteger(self):
        return isinstance(self.x, int) and isinstance(self.y, int)


E = Point(1, 0)
S = Point(0, 1)
W = Point(-1, 0)
N = Point(0, -1)

NE = Point(1, -1)
NW = Point(-1, -1)
SE = Point(1, 1)
SW = Point(-1, 1)


directions = [
    Point(-1, -1),
    Point(0, -1),
    Point(1, -1),
    Point(-1, 0),
    Point(1, 0),
    Point(-1, 1),
    Point(0, 1),
    Point(1, 1),
]
