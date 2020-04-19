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

    def get_slope_from_origin(self, target=0):
        return (self.y - target.y) / (self.x - target.x)

    def get_line_to(self, point):
        slope = self.get_slope_from_origin(point)
        print("y = {0}x + {1}".format(slope, point.y - slope * point.x))
        return slope, point.y - slope * point.x


print(Point(7, 2).reflect_x())
print(Point(8, 21).get_line_to(Point(9, 22)))
print(Point(4, 11).get_line_to(Point(6, 15)))