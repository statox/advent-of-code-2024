class Point:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(f"{self.x};{self.y}")

    def isInBound(self, bound):
        return self.x >= 0 and self.y >= 0 and self.x <= bound.x and self.y <= bound.y


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
