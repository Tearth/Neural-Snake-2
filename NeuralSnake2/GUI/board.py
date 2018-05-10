from field import *

class Board(object):
    def __init__(self, width, height):
        self._width = width
        self._height = height

        self._fields = [Field.NONE] * width
        for i in range(self._width):
            self._fields[i] = [Field.NONE] * height

    def draw(self, canvas):
        canvas.delete("all")