class vector2d(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return vector2d(self.x + other.x, self.y + other.y)