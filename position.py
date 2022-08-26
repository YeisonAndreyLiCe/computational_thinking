
class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Position(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def move(self, delta_x, delta_y):
        return Position(self.x + delta_x, self.y + delta_y)

    def distance(self, other_coordinate):
        delta_x = other_coordinate.x - self.x
        delta_y = other_coordinate.y - self.y
        return (delta_x**2 + delta_y**2)**0.5
