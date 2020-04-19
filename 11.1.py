class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def get_distance(self, target=0):
        return ((self.x - target.x) ** 2 + (self.y - target.y) ** 2) ** 0.5

    def reflect_x(self):
        return Point(self.x, -self.y)

print(Point(5, 1).reflect_x())
