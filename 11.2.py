# ex 11.2.6


class Rectangle:

    def __init__(self, posn, x, y):
        self.width = x
        self.height = y
        self.corner = posn

    def __str__(self):
        return "({0}, {1})".format(self.width, self.height, self.corner)

    def area(self):
        return self.width * self.height

    def perimiter(self):
        return (self.width + self.height) * 2

    def flip(self):
        (self.height, self.width) = (self.width, self.height)


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

r = Rectangle(Point(100, 50), 10, 5)

r.flip()

print(r.flip())